import re
from typing import List, Dict, Tuple, Set
from collections import defaultdict

def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Calcola la distanza di Levenshtein tra due stringhe.
    
    Args:
        str1: Prima stringa
        str2: Seconda stringa
        
    Returns:
        Distanza di Levenshtein come intero
    """
    # Ottimizzazione: verifica rapida per escludere parole con differenza di lunghezza eccessiva
    if abs(len(str1) - len(str2)) > 2:
        return 3  # Restituisce un valore superiore a max_distance
    
    # Implementazione ottimizzata della distanza di Levenshtein
    # Usa solo due righe della matrice invece che l'intera matrice
    m, n = len(str1), len(str2)
    
    # Inizializza le due righe
    previous_row = list(range(n + 1))
    current_row = [0] * (n + 1)
    
    for i in range(1, m + 1):
        current_row[0] = i
        
        for j in range(1, n + 1):
            deletion = previous_row[j] + 1
            insertion = current_row[j - 1] + 1
            substitution = previous_row[j - 1]
            
            if str1[i - 1] != str2[j - 1]:
                substitution += 1
                
            current_row[j] = min(deletion, insertion, substitution)
        
        # Scambia le righe per la prossima iterazione
        previous_row, current_row = current_row, previous_row
    
    return previous_row[n]

def create_word_groups(dictionary: Set[str]) -> Dict[str, List[str]]:
    """
    Raggruppa le parole per la prima lettera e la lunghezza per velocizzare la ricerca.
    
    Args:
        dictionary: Set di parole corrette
        
    Returns:
        Dizionario con chiavi (lettera iniziale, lunghezza) e liste di parole
    """
    word_groups = defaultdict(list)
    
    for word in dictionary:
        if word:
            # Raggruppa per prima lettera e lunghezza della parola
            key = (word[0], len(word))
            word_groups[key].append(word)
    
    return word_groups

def find_corrections(word: str, dictionary: Set[str], word_groups: Dict, max_distance: int = 2) -> List[Tuple[str, int]]:
    """
    Trova possibili correzioni per una parola nel dizionario.
    
    Args:
        word: Parola da correggere
        dictionary: Set di parole corrette
        word_groups: Gruppi di parole per ricerca efficiente
        max_distance: Distanza massima di Levenshtein da considerare
        
    Returns:
        Lista di tuple (parola corretta, distanza) ordinate per distanza
    """
    word_lower = word.lower()
    
    # Se la parola è già corretta, restituisci la parola stessa
    if word_lower in dictionary:
        return [(word, 0)]
    
    corrections = []
    word_len = len(word_lower)
    
    # Controlla solo parole con lunghezza simile e stessa lettera iniziale (o vicine)
    potential_first_chars = [c for c in 'abcdefghijklmnopqrstuvwxyz' if abs(ord(c) - ord(word_lower[0])) <= 1] if word_lower else []
    
    for length in range(max(1, word_len - max_distance), word_len + max_distance + 1):
        for first_char in [word_lower[0]] + potential_first_chars:
            key = (first_char, length)
            
            if key in word_groups:
                for dict_word in word_groups[key]:
                    distance = levenshtein_distance(word_lower, dict_word)
                    if distance <= max_distance:
                        corrections.append((dict_word, distance))
    
    # Ordina per distanza di Levenshtein e poi alfabeticamente
    return sorted(corrections, key=lambda x: (x[1], x[0]))

def correct_text(text: str, dictionary: Set[str], max_distance: int = 2) -> Tuple[str, List[Dict]]:
    """
    Corregge gli errori lessicali in un testo usando la distanza di Levenshtein.
    
    Args:
        text: Testo da correggere
        dictionary: Set di parole corrette
        max_distance: Distanza massima di Levenshtein da considerare
        
    Returns:
        Testo corretto e lista di errori trovati
    """
    # Pre-calcola i gruppi di parole per velocizzare la ricerca
    word_groups = create_word_groups(dictionary)
    
    words = re.findall(r'\b[A-Za-z\']+\b', text)
    errors = []
    corrected_text = text
    
    # Tieni traccia delle parole già controllate per evitare duplicati
    checked_words = set()
    
    # Trova e correggi gli errori
    for word in words:
        word_lower = word.lower()
        
        # Ignora parole brevi, numeri o già controllate
        if len(word) <= 1 or word.isdigit() or word_lower in checked_words:
            continue
        
        checked_words.add(word_lower)
        
        # Trova le possibili correzioni
        potential_corrections = find_corrections(word, dictionary, word_groups, max_distance)
        
        # Se abbiamo trovato correzioni
        if potential_corrections and potential_corrections[0][1] > 0:
            best_correction = potential_corrections[0][0]
            distance = potential_corrections[0][1]
            
            # Preserva la capitalizzazione originale
            if word[0].isupper():
                best_correction = best_correction.capitalize()
            
            # Aggiungi all'elenco degli errori
            errors.append({
                "original": word,
                "correction": best_correction,
                "distance": distance
            })
            
            # Correggi nel testo (rispettando i confini delle parole)
            corrected_text = re.sub(r'\b' + re.escape(word) + r'\b', best_correction, corrected_text)
    
    # Ordina gli errori per gravità (distanza)
    errors.sort(key=lambda x: x["distance"], reverse=True)
    
    return corrected_text, errors

# Esempio di utilizzo
if __name__ == "__main__":
    import time
    
    # Misura il tempo di esecuzione
    start_time = time.time()
    
    # Carica il dizionario come un set (importante!)
    with open('/usr/share/dict/british-english', 'r') as correct:
        english_words = {word.strip().lower() for word in correct.readlines()}
    
    # Testo di esempio con errori lessicali
    sample_text = """Las weak, I visitted a musuem that exhebits artefacts from anchient civilasations. The expereance was incrediblle, but som of the descripshons were dificult to undrestand becose of the olden stile of writting. I noteced that som historicle detales were exagerrated, espeshally about the Midle Ege kings who were portraiyed as infallibel.
A tour guied explaind the orrigin of certain relics, but he mispronunce som names, which confuzed me. One of the most intresting artefacts was a gilden statue of a Mithologicol creture that resembeled a griffen, but with unussualy large wings.
After the tour, I went to a libary to reserch more about anchient architechture and the technics used to construct massiv monumments like the Pyramides and the Colossium. I found a manuskript from the 17th sentury that detalied the metalls used in medeviel weaponry, but it was writen in an arkaic dialect, making it extremly complex to interpret.
I desided to barrow a book about linguistics to undrestand how languges evlove over time. One chapther expained the diffirences betwen Latin and its derivitives, but the exampels were poorly formated, making the comparisons uncler.
Overall, it was an edducational but chalenging day, and I realy apperciate how our knowlege of history continuasly expands through new discoveries and reserch."""
    
    print(f"Dimensione del dizionario: {len(english_words)} parole")
    
    # Esegui la correzione
    corrected_text, errors = correct_text(sample_text, english_words)
    
    # Tempo totale
    elapsed_time = time.time() - start_time
    
    # Stampa i risultati
    print("Testo originale:")
    print(sample_text)
    print("\nTesto corretto:")
    print(corrected_text)
    print("\nErrori trovati (ordinati per gravità):")
    for error in errors:
        print(f'"{error["original"]}" → "{error["correction"]}" (Distanza: {error["distance"]})')
    
    # Statistiche
    print(f"\nStatistiche:")
    print(f"Numero totale di errori trovati: {len(errors)}")
    print(f"Tempo di esecuzione: {elapsed_time:.2f} secondi")
    
    # Distribuzione della distanza
    distance_counts = {}
    for error in errors:
        dist = error["distance"]
        distance_counts[dist] = distance_counts.get(dist, 0) + 1
            
    print("Distribuzione degli errori per distanza di Levenshtein:")
    for dist, count in sorted(distance_counts.items()):
        print(f"Distanza {dist}: {count} errori")