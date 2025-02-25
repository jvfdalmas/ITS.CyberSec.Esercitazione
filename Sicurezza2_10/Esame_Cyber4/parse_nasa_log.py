import re
from collections import Counter, defaultdict

def parse_nasa_log(file_path):
    """
    Analizza il file di log NASA e restituisce statistiche chiave,
    distinguendo tra pagine statiche e dinamiche e identificando possibili minacce.
    
    Analisi effettuate:
      - Dati di supporto:
          * Numero totale di richieste.
          * Top IP e pagine più visitate.
          * Top 10 pagine statiche e dinamiche (escludendo le immagini per certe sezioni).
          * Distribuzione dei codici di stato HTTP.
      - Analisi Cybersecurity:
          * IP con errori 404.
          * IP sospetti (per codici di stato 403, 500, 503).
          * IP con accessi in orari non usuali (20:00 - 08:00).
          * IP sospetti per flooding (numero massimo di richieste in un minuto, soglia > 30).
          * Top 5 IP che hanno scaricato la maggiore quantità di dati.
          * Analisi dei metodi HTTP sospetti (diversi da GET e POST) con i 10 IP che hanno effettuato più richieste per ciascun metodo.
      - Analisi dei Pattern di Accesso per Risorsa:
          * Per ciascuna risorsa viene calcolato il numero totale di richieste,
            il numero di IP distinti che l'hanno richiesta e i 3 IP principali per tale risorsa.
    """
    # Inizializzazione dei contatori e dizionari
    total_requests = 0
    ip_counter = Counter()
    page_counter = Counter()
    static_pages_counter = Counter()
    dynamic_pages_counter = Counter()
    hourly_counter = Counter()
    status_code_counter = Counter()
    error_404_counter = Counter()
    ip_status_codes = defaultdict(Counter)
    offhours_ips = Counter()
    ip_bytes_downloaded = defaultdict(int)  # Totale bytes scaricati per IP

    # Per il rilevamento del flooding: conta richieste per ogni IP per minuto
    ip_minute_access = defaultdict(int)
    FLOODING_THRESHOLD = 30  # soglia: più di 30 richieste nello stesso minuto

    # Analisi dei metodi HTTP
    method_counter = Counter()
    # Per i metodi sospetti (diversi da GET e POST), mappa metodo -> (IP -> count)
    suspicious_methods = defaultdict(Counter)
    common_methods = {"GET", "POST"}

    # Analisi dei pattern di accesso per risorsa
    resource_access = defaultdict(lambda: {"count": 0, "ips": Counter()})

    # Definizione delle estensioni per pagine statiche e dinamiche
    static_extensions = {".html", ".htm", ".css", ".js", ".jpg", ".png", ".gif", ".ico", ".txt", ".pdf"}
    dynamic_extensions = {".cgi", ".php", ".asp", ".jsp", ".pl", ".py"}

    # Espressione regolare per estrarre i campi:
    # Cattura: IP, data, ora, metodo, pagina, codice di stato e dimensione.
    log_pattern = re.compile(
        r'(\S+) - - \[(\d{2})/(\w{3})/(\d{4}):'
        r'(\d{2}):(\d{2}):(\d{2}) [^]]+\] "(\S+) (\S+) HTTP/\d\.\d" '
        r'(\d{3}) (\d+|-)'
    )

    with open(file_path, "r", encoding="latin-1") as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                # Estrazione dei campi
                ip, day, month, year, hour, minute, second, method, page, status, size = match.groups()
                total_requests += 1

                # Dati di supporto
                ip_counter[ip] += 1
                page_counter[page] += 1
                hourly_counter[hour] += 1
                status_code_counter[status] += 1
                ip_status_codes[ip][status] += 1

                # Aggiornamento analisi dei metodi HTTP
                method_counter[method] += 1
                if method not in common_methods:
                    suspicious_methods[method][ip] += 1

                # Accumulo dei byte scaricati (se il campo size non è "-")
                if size != "-":
                    try:
                        ip_bytes_downloaded[ip] += int(size)
                    except ValueError:
                        pass

                # Classificazione in pagine statiche o dinamiche
                lower_page = page.lower()
                if any(lower_page.endswith(ext) for ext in static_extensions):
                    static_pages_counter[page] += 1
                elif any(lower_page.endswith(ext) for ext in dynamic_extensions):
                    dynamic_pages_counter[page] += 1

                # Aggiornamento dell'analisi dei pattern di accesso per risorsa
                resource_access[page]["count"] += 1
                resource_access[page]["ips"][ip] += 1

                # Errori 404
                if status == "404":
                    error_404_counter[ip] += 1

                # Accessi in orari non usuali (off-hours: 20:00 - 08:00)
                hour_int = int(hour)
                if hour_int >= 20 or hour_int < 8:
                    offhours_ips[ip] += 1

                # Aggregazione per flooding: chiave composta da IP e timestamp al minuto
                minute_key = f"{ip}_{day}/{month}/{year}:{hour}:{minute}"
                ip_minute_access[minute_key] += 1

    # Flooding: per ciascun IP, determina il massimo di richieste in un singolo minuto (se supera la soglia)
    flooding_ips = defaultdict(int)
    for key, count in ip_minute_access.items():
        ip = key.split("_")[0]
        if count > FLOODING_THRESHOLD:
            flooding_ips[ip] = max(flooding_ips[ip], count)

    # Codici di stato sospetti (403, 500, 503)
    suspicious_status_codes = {"403", "500", "503"}
    ip_suspicious_status = {
        ip: sum(cnt for code, cnt in statuses.items() if code in suspicious_status_codes)
        for ip, statuses in ip_status_codes.items()
    }
    top_suspicious_ips_status = sorted(ip_suspicious_status.items(), key=lambda x: x[1], reverse=True)[:5]

    # Top 5 IP che hanno scaricato la maggiore quantità di dati
    top_downloaders = sorted(ip_bytes_downloaded.items(), key=lambda x: x[1], reverse=True)[:5]

    # Analisi dei pattern di accesso per risorsa:
    # Creiamo una lista ordinata delle risorse in base al numero totale di richieste.
    resource_patterns = []
    for resource, data in resource_access.items():
        total = data["count"]
        distinct_ips = len(data["ips"])
        # Prendiamo i 3 IP con più richieste per questa risorsa
        top_ips = sorted(data["ips"].items(), key=lambda x: x[1], reverse=True)[:3]
        resource_patterns.append((resource, total, distinct_ips, top_ips))
    resource_patterns = sorted(resource_patterns, key=lambda x: x[1], reverse=True)[:10]

    return {
        "total_requests": total_requests,
        "top_ips": ip_counter.most_common(10),
        "top_pages": page_counter.most_common(10),
        "top_static_pages": static_pages_counter.most_common(10),
        "top_dynamic_pages": dynamic_pages_counter.most_common(10),
        "top_status_codes": status_code_counter.most_common(),
        "error_404_ips": error_404_counter.most_common(10),
        "suspicious_ips_status": top_suspicious_ips_status,
        "offhours_ips": offhours_ips.most_common(10),
        "flooding_ips": sorted(flooding_ips.items(), key=lambda x: x[1], reverse=True),
        "top_downloaders": top_downloaders,
        "method_counter": method_counter,
        "suspicious_methods": {method: dict(ips) for method, ips in suspicious_methods.items()},
        "resource_patterns": resource_patterns
    }

def save_report(stats, output_file):
    """Salva il report in un file di testo leggibile, suddividendo in varie sezioni."""
    # Definizione delle estensioni di immagini da escludere
    image_extensions = (".jpg", ".png", ".gif", ".ico")

    # Filtra le pagine escludendo le immagini (confronto in lowercase)
    filtered_top_pages = [(page, count) for page, count in stats['top_pages'] 
                          if not page.lower().endswith(image_extensions)]
    filtered_top_static_pages = [(page, count) for page, count in stats['top_static_pages'] 
                                 if not page.lower().endswith(image_extensions)]

    with open(output_file, "w", encoding="utf-8") as f:
        # Introduzione generale
        f.write("#################### REPORT DI ANALISI LOG ####################\n\n")
        f.write("Questo report è stato generato per analizzare il file di log e rilevare anomalie e possibili minacce alla sicurezza informatica. Il report è suddiviso in due sezioni:\n\n")
        f.write("1. Dati di Supporto\n")
        f.write("2. Analisi Cybersecurity\n\n")
        
        # Sezione 1: Dati di Supporto
        f.write("#################### SEZIONE 1: DATI DI SUPPORTO ####################\n\n")
        f.write(f"Numero totale di richieste: {stats['total_requests']}\n\n")
        
        f.write("---- Top 10 IP più attivi ----\n\n")
        for ip, count in stats['top_ips']:
            f.write(f"{ip}: {count} richieste\n")
        f.write("\n")
        
        f.write("---- Top 10 pagine più visitate ----\n")
        f.write("Nota: Le immagini sono state escluse dall'analisi per la cybersecurity.\n\n")
        for page, count in filtered_top_pages:
            f.write(f"{page}: {count} visite\n")
        f.write("\n")
        
        f.write("---- Top 10 pagine statiche ----\n")
        f.write("Nota: Le immagini sono state escluse dall'analisi per la cybersecurity.\n\n")
        for page, count in filtered_top_static_pages:
            f.write(f"{page}: {count} visite\n")
        f.write("\n")
        
        f.write("---- Top 10 pagine dinamiche ----\n\n")
        for page, count in stats['top_dynamic_pages']:
            f.write(f"{page}: {count} visite\n")
        f.write("\n")
        
        f.write("---- Distribuzione codici di stato HTTP ----\n\n")
        for code, count in stats['top_status_codes']:
            f.write(f"{code}: {count}\n")
        f.write("\n")
        
        # Sezione 2: Analisi Cybersecurity
        f.write("#################### SEZIONE 2: ANALISI CYBERSECURITY ####################\n\n")
        
        f.write("---- IP con errori 404 ----\n\n")
        f.write("Questa sezione mostra gli IP che hanno causato errori 404, indicando che hanno richiesto pagine non esistenti. Questi IP potrebbero essere potenziali attaccanti che tentano di accedere a risorse inesistenti.\n\n")
        for ip, count in stats['error_404_ips']:
            f.write(f"{ip}: {count} errori 404\n")
        f.write("\n")
        
        f.write("---- IP sospetti (per codici di stato 403, 500, 503) ----\n\n")
        f.write("Questa sezione evidenzia gli IP che hanno ricevuto codici di stato HTTP critici (403, 500, 503), indicativi di possibili tentativi di attacco o malfunzionamenti del server.\n\n")
        for ip, count in stats['suspicious_ips_status']:
            f.write(f"{ip}: {count} codici critici\n")
        f.write("\n")
        
        f.write("---- IP con accessi in orari non usuali (20:00 - 08:00) ----\n\n")
        f.write("Questa sezione mostra gli IP che hanno effettuato accessi in orari non usuali, il che potrebbe indicare attività sospette o tentativi di attacchi fuori dall'orario lavorativo.\n\n")
        for ip, count in stats['offhours_ips']:
            f.write(f"{ip}: {count} accessi in orari non usuali\n")
        f.write("\n")
        
        f.write("---- IP sospetti per flooding ----\n\n")
        f.write("Il criterio adottato è di segnalare un IP se in almeno un minuto ha superato le 30 richieste. Per ciascun IP viene riportato il picco massimo di richieste registrato in un singolo minuto.\n\n")
        for ip, max_requests in stats['flooding_ips']:
            f.write(f"{ip}: {max_requests} richieste in un minuto\n")
        f.write("\n")
        
        f.write("---- Top 5 IP con maggiore quantità di dati scaricati ----\n\n")
        f.write("Questa sezione mostra i 5 IP che hanno trasferito la maggiore quantità di dati. Un elevato volume di dati scaricati potrebbe indicare attività di scraping, download massivo o altri comportamenti sospetti.\n\n")
        for ip, bytes_downloaded in stats['top_downloaders']:
            f.write(f"{ip}: {bytes_downloaded} bytes\n")
        f.write("\n")
        
        f.write("---- Analisi dei Metodi HTTP Sospetti ----\n\n")
        f.write("Questa sezione analizza l'uso dei metodi HTTP. Vengono considerati sospetti i metodi diversi da GET e POST, poiché potrebbero indicare tentativi di manipolare risorse o configurazioni.\n\n")
        if not stats['suspicious_methods']:
            f.write("Nessun metodo HTTP sospetto è stato utilizzato.\n")
        else:
            for method, ip_dict in stats['suspicious_methods'].items():
                total_method = stats['method_counter'][method]
                f.write(f"Metodo {method}: {total_method} richieste\n")
                # Prendi i 10 IP con più richieste per questo metodo
                top_ips_method = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)[:10]
                f.write("IP coinvolti (top 10):\n")
                for ip, count in top_ips_method:
                    f.write(f"  - {ip}: {count} richieste\n")
                f.write("\n")
        
        f.write("----  Analisi dei Pattern di Accesso per Risorsa ----\n\n")
        f.write("In questa sezione vengono analizzate le risorse richieste, indicando per ciascuna il numero totale di accessi, il numero di IP distinti e i 3 IP principali che hanno effettuato richieste.\n")
        f.write("Le risorse ripetutamente richieste possono rappresentare un bersaglio di scraping o tentativi di accesso non autorizzati.\n\n")
        if not stats["resource_patterns"]:
            f.write("Nessuna risorsa analizzata.\n")
        else:
            for resource, total, distinct_ips, top_ips in stats["resource_patterns"]:
                f.write(f"Risorsa: {resource}\n")
                f.write(f"  - Totale accessi: {total}\n")
                f.write(f"  - Numero di IP distinti: {distinct_ips}\n")
                f.write("  - Top 3 IP:\n")
                for ip, count in top_ips:
                    f.write(f"      * {ip}: {count} accessi\n")
                f.write("\n")
        
        f.write("#################### FINE REPORT ####################\n")

# Esegui l'analisi (modifica il percorso se necessario)
log_file_path = "NASA_access_log_Aug95"
output_file = "nasa_log_report.txt"

stats = parse_nasa_log(log_file_path)
save_report(stats, output_file)
print(f"Report salvato in {output_file}")
