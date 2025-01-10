import requests
import json

base_url = "http://127.0.0.1:8080/"

print("Benvenuti")

iFlag = 0
while iFlag == 0:

    print("\nServizi disponibili:")
    print("1. Cerca Casa Vendita")
    print("2. Cerca Casa Affitto")
    print("3. Venduta Casa")
    print("4. Affittata Casa")
    print("5. Report di Marketing")
    print("6. Cerca Filiale")
    print("7. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if iOper == 1:
        print("Cerca Casa Vendita")
        metri_min = input("Inserire i metri minimi: ")
        prezzo_max = input("Inserire il prezzo massimo: ")
        stato = input("Inserire lo stato (LIBERO/OCCUPATO): ")
        params = {
            "metri_min": metri_min,
            "prezzo_max": prezzo_max,
            "stato": stato
        }
        response = requests.get(base_url + "cerca_casa_vendita", params=params, verify=False)
        if response.status_code == 200:
            print("Case trovate:")
            print(json.dumps(response.json(), indent=4))
        else:
            print("Errore nella ricerca delle case in vendita.")

    elif iOper == 2:
        print("Cerca Casa Affitto")
        tipo_affitto = input("Inserire il tipo di affitto (PARZIALE/TOTALE): ")
        prezzo_max = input("Inserire il prezzo massimo: ")
        params = {
            "tipo_affitto": tipo_affitto,
            "prezzo_max": prezzo_max
        }
        response = requests.get(base_url + "cerca_casa_affitto", params=params, verify=False)
        if response.status_code == 200:
            print("Case trovate:")
            print(json.dumps(response.json(), indent=4))
        else:
            print("Errore nella ricerca delle case in affitto.")

    elif iOper == 3:
        print("Venduta Casa")
        catastale = input("Inserire il catastale: ")
        data_vendita = input("Inserire la data di vendita (AAAA-MM-GG): ")
        filiale_proponente = input("Inserire la filiale proponente: ")
        filiale_venditrice = input("Inserire la filiale venditrice: ")
        prezzo_vendita = input("Inserire il prezzo di vendita: ")
        data = {
            "catastale": catastale,
            "data_vendita": data_vendita,
            "filiale_proponente": filiale_proponente,
            "filiale_venditrice": filiale_venditrice,
            "prezzo_vendita": prezzo_vendita
        }
        response = requests.post(base_url + "venduta_casa", json=data, verify=False)
        if response.status_code == 200:
            print("Casa registrata come venduta con successo.")
        else:
            print("Errore nella registrazione della vendita della casa.")

    elif iOper == 4:
        print("Affittata Casa")
        catastale = input("Inserire il catastale: ")
        data_affitto = input("Inserire la data di affitto (AAAA-MM-GG): ")
        filiale_proponente = input("Inserire la filiale proponente: ")
        filiale_venditrice = input("Inserire la filiale venditrice: ")
        prezzo_affitto = input("Inserire il prezzo di affitto mensile: ")
        durata_contratto = input("Inserire la durata del contratto (in mesi): ")
        data = {
            "catastale": catastale,
            "data_affitto": data_affitto,
            "filiale_proponente": filiale_proponente,
            "filiale_venditrice": filiale_venditrice,
            "prezzo_affitto": prezzo_affitto,
            "durata_contratto": durata_contratto
        }
        response = requests.post(base_url + "affittata_casa", json=data, verify=False)
        if response.status_code == 200:
            print("Casa registrata come affittata con successo.")
        else:
            print("Errore nella registrazione dell'affitto della casa.")

    elif iOper == 5:
        print("Report di Marketing")
        start_date = input("Inserire la data di inizio (AAAA-MM-GG): ")
        end_date = input("Inserire la data di fine (AAAA-MM-GG): ")
        params = {
            "start_date": start_date,
            "end_date": end_date
        }
        response = requests.get(base_url + "report_marketing", params=params, verify=False)
        if response.status_code == 200:
            report = response.json()
            print("Report di Marketing:")
            print(json.dumps(report, indent=4))
            with open("report_marketing.json", "w") as file:
                json.dump(report, file, indent=4)
            print("Report salvato in 'report_marketing.json'.")
        else:
            print("Errore nel generare il report di marketing.")

    elif iOper == 6:
        print("Cerca Filiale")
        nome = input("Inserire parte del nome della filiale: ")
        params = {"nome": nome}
        response = requests.get(base_url + "cerca_filiale", params=params, verify=False)
        if response.status_code == 200:
            print("Filiali trovate:")
            print(json.dumps(response.json(), indent=4))
        elif response.status_code == 404:
            print("Nessuna filiale trovata con il nome fornito.")
        else:
            print("Errore nella ricerca della filiale.")

    elif iOper == 7:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")
