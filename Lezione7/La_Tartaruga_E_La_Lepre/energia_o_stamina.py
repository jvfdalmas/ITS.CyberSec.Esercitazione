""" 2. Energia o Stamina:
Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. L'energia inziale per entrambi gli animali è 100.

Nuove regole di movimento:
- Tartaruga:
    - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia.
    - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
    - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

- Lepre:
    - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energiza iniziale.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
    - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
"""
import random

race_track_len: int = 70 # percorso della corsa
race_track: list = ["_" for _ in range(0, race_track_len)] # corsa
tortoise: int = 1 # posizione iniziale - tortoise
tortoise_stamina: int = 100 # stamina iniziale - tortoise
rabbit: int = 1 # posizione iniziale - rabbit
rabbit_stamina: int = 100 # stamina iniziale - rabbit
clock: int = 0 # counter di mose | secondi
weather: str = "soleggiato"  #  weather iniziale

def tortoise_move(tortoise, stamina, weather) -> int:
    i: int = random.randint(1,10)

    if 1 <= i <= 5: # 50% di probabilità: passo veloce: avanza di 3 quadrati e richede 5 di energia
        if stamina > 5:
            tortoise += 3
            stamina -= 5
        else:
            stamina += 10 # guadagna 10 di energia se la mossa non è possibile
    elif 6 <= i <= 7: # 20% di probabilità: Scivolata: arretra di 6 quadrati e richede 10 di energia
        if stamina > 10:
            tortoise -= 6
            stamina -= 10
        else:
            stamina += 10 # guadagna 10 di energia se la mossa non è possibile
    elif 7 <= i <= 10: # 30% di probabilità: Passo lento: avanza di 1 quadrato e richiede 3 di energia
        if stamina > 3:
            tortoise += 1
            stamina -= 3
        else:
            stamina += 10 # guadagna 10 di energia se la mossa non è possibile
    
    if weather == 'pioggia': # rainny weather changes movement value 
        tortoise -= 1

    tortoise = min(max(1, tortoise), 70) # assecure postion between 1 and 70
    stamina = min(max(1, stamina), 100) # assecure stamina between 1 and 100

    return tortoise, stamina
    

def rabbit_move(rabbit: int, stamina: int, weather: str):
    i: int = random.randint(1,10)

    if 1 <= i <= 2: # 20% di probabilità: non si muove e recupera 10 di energia.
        stamina += 10
    elif 3 <= i <= 4: # 20% di probabilità: grande balzo: avanza di 9 quadrati e richiede 15 di energia
        if stamina > 15:
            rabbit += 9
            stamina -= 15
    elif i == 5: # 10% di probabilità: grande scivolata: arretra di 12 quadrati e richiede 20 di energia
        if stamina > 20:
            rabbit -= 12
            stamina -= 20
    elif 6 <= i <= 8: # 20% di probabilità: piccolo balzo: avanza di 1 quadrato e richiede 5 di energia
        if stamina > 5:
            rabbit += 1
            stamina -= 5
    elif 9 <= i <= 10: # 20% di probabilità: piccola scivolata:avanza di 1 quadrato e richiede 3 di energia.
        if stamina > 8:
            rabbit -= 8
            stamina -= 2

    if weather == 'pioggia': # rainny weather changes movement value 
        rabbit -= 2

    rabbit = min(max(1, rabbit), 70)  # assecure postion between 1 and 70
    stamina = min(max(1, stamina), 100) # assecure stamina between 1 and 100

    return rabbit, stamina
        
def change_weather(weather: str, clock: int) -> str:
    if clock != 0 and clock % 10 == 0: # weather changes (each 10 seconds) according to the clock 
        if weather == 'soleggiato':
            return "pioggia"
        else:
            return 'soleggiato'
    else:
        return weather

def corsia_di_gara(race_track: list, rabbit: int, rabbit_stamina: int, tortoise: int, tortoise_stamina: int, weather: str, clock) -> str:
        
    for i in range(len(race_track)): # cleans the last position
        if race_track[i] in ['OUCH!!!', 'H', 'T', 'T\H']:
            race_track[i] = '_'
    
    if rabbit == tortoise: # update racers position in race track
        if clock != 0:
            race_track[rabbit-1] = 'OUCH!!!'
        else:
            race_track[0] = 'T\H'
    else:
        race_track[rabbit-1] = "H"
        race_track[tortoise-1] = "T"

    # prints updated race track
    print("\n", "\n", " ".join(race_track), end="")
    print(f"\n rabbit position: {rabbit} / rabbit stamina: {rabbit_stamina} / tortoise position: {tortoise} / tortoise stamina: {tortoise_stamina} / weather: {weather} / elapsed time: {clock} sec", end="")
    
    # prints the winner
    if rabbit == 70 and tortoise == 70:
        print("\n","IT'S A TIE.", end="")
    elif race_track[69] == "T":
        print("\n","TORTOISE WINS! || VAY!!!", end="")
    elif race_track[69] == "H":
        print("\n","HARE WINS || YUCH!!!", end="")



print("BANG !!!!! AND THEY'RE OFF !!!!!")

while race_track[69] == "_":
    corsia_di_gara(race_track, rabbit, rabbit_stamina, tortoise, tortoise_stamina, weather, clock)
    clock += 1
    weather = change_weather(weather, clock)
    rabbit, rabbit_stamina = rabbit_move(rabbit, rabbit_stamina, weather)
    tortoise, tortoise_stamina = tortoise_move(tortoise, tortoise_stamina, weather)

print(f"The race took {clock} seconds")