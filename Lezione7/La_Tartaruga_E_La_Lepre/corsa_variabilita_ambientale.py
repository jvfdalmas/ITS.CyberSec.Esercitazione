"""" Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
- La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
- La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
"""

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







