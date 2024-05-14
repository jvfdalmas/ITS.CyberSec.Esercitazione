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

from random import choices

def turtle_race():
    turtle_steps:list = [3, -6, 1]
    turtle_steps_probability:list = [0.5, 0.2, 0.3]
    turtle_move = choices(turtle_steps, turtle_steps_probability)
    turtle_track_race:list = [numero for numero in range(1,71)]
    turtle_clock: int = 0
    turtle_track_race[0] = "turtle"

    while turtle_track_race[69] != "turtle":
        
        turtle_move: list = choices(turtle_steps, turtle_steps_probability)
        turtle_move: int = int(turtle_move[0])
        last_index: int = turtle_track_race.index("turtle")
        turtle_track_race[last_index] = last_index + 1
        turtle_clock += 1
        
        if last_index + turtle_move <= 0:
            turtle_track_race[0] = "turtle"
        if last_index + turtle_move >= 69:
            turtle_track_race[69] = "turtle"
        else:
            turtle_track_race[last_index + turtle_move] = "turtle"
        
    return turtle_clock

def rabbit_race():
    rabbit_steps:list = [3, -6, 1]
    rabbit_steps_probability:list = [0.5, 0.2, 0.3]
    rabbit_move = choices(rabbit_steps, rabbit_steps_probability)
    rabbit_track_race:list = [numero for numero in range(1,71)]
    rabbit_clock: int = 0
    rabbit_track_race[0] = "rabbit"

    while rabbit_track_race[69] != "rabbit":
        
        rabbit_move: list = choices(rabbit_steps, rabbit_steps_probability)
        rabbit_move: int = int(rabbit_move[0])
        last_index: int = rabbit_track_race.index("rabbit")
        rabbit_track_race[last_index] = last_index + 1
        rabbit_clock += 1
        
        if last_index + rabbit_move <= 0:
            rabbit_track_race[0] = "rabbit"
        if last_index + rabbit_move >= 69:
            rabbit_track_race[69] = "rabbit"
        else:
            rabbit_track_race[last_index + rabbit_move] = "rabbit"
        
    return rabbit_clock

def rabbit_turtle_race():
    clock_rabbit_race: int = rabbit_race()
    clock_turtle_race: int = turtle_race()

    if clock_rabbit_race == clock_turtle_race:
        return f"Both turtle and rabbit arrived together after {clock_rabbit_race} seconds. It is a tie!"
    elif clock_rabbit_race <= clock_turtle_race:
        return f"Rabbit won!!!! It took rabbit {clock_rabbit_race} seconds, while the turtle arrived after {clock_turtle_race} seconds."
    elif clock_rabbit_race >= clock_turtle_race:
        return f"Turtle won!!! It took rabbit {clock_rabbit_race} seconds, while the turtle arrived after {clock_turtle_race} seconds."

print(rabbit_turtle_race())







