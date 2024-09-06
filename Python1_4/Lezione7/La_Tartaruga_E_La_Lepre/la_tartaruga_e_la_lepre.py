""" In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine dell
a gara. """

import random

race_track_len: int = 70 # percorso della corsa
race_track: list = ["_" for position in range(0, race_track_len)] # corsa
tortoise: int = 1 # posizione iniziale - tortoise
rabbit: int = 1 # posizione iniziale - rabbit
clock: int = 0 # counter di mose | secondi

def tortoise_move() -> int:
    i: int = random.randint(1,10)

    if 1 <= i <= 5: # 50% di probabilità
        return 3 # Passo veloce: avanza di 3 quadrati
    elif 6 <= i <= 7: # 20% di probabilità
        return -6 # Scivolata: arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    elif 7 <= i <= 10: # 30% di probabilità
        return 1 # Passo lento: avanza di 1 quadrato

def rabbit_move():
    i: int = random.randint(1,10)

    if 1 <= i <= 2: # 20% di probabilità
        return 0# non si muove.
    elif 3 <= i <= 4: # 20% di probabilità
        return 9 # grande balzo: avanza di 9 quadrati
    elif i == 5: # 10% di probabilità
        return -12 # grande scivolata: arretra di 12 quadrati
    elif 6 <= i <= 8: # 20% di probabilità
        return 1 # piccolo balzo: avanza di 1 quadrato
    elif 9 <= i <= 10: # 20% di probabilità
        return -2 # piccola scivolata: arretra di 2 quadrati

def corsia_di_gara(race_track: list, rabbit: int, tortoise: int):
    # cleans the last position
    for i in range(len(race_track)):
        if race_track[i] in ['OUCH!!!', 'H', 'T']:
            race_track[i] = '_'
    
    # rabbit stays inside the race track
    rabbit = max(1, rabbit)
    rabbit = min(rabbit, 70)
    
    # tortoise stays inside the race track
    tortoise = max(1, tortoise)
    tortoise = min(tortoise, 70)

    # update racers position in race track
    if rabbit == tortoise:
        race_track[rabbit-1] = 'OUCH!!!'
    else:
        race_track[rabbit-1] = "H"
        race_track[tortoise-1] = "T"

    # prints updated race track
    print(" ".join(race_track), f"rabbit position: {rabbit} / tortoise position: {tortoise}")
    
    # prints the winner
    if rabbit == 70 and tortoise == 70:
        print("IT'S A TIE.")
    elif race_track[69] == "T":
        print("TORTOISE WINS! || VAY!!!")
    elif race_track[69] == "H":
        print("HARE WINS || YUCH!!!")

print("BANG !!!!! AND THEY'RE OFF !!!!!")

while race_track[69] == "_":
    clock += 1
    rabbit += rabbit_move()
    tortoise += tortoise_move()
    corsia_di_gara(race_track, rabbit, tortoise)

print(f"The race took {clock} seconds")






