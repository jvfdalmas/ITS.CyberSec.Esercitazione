"""3. Ostacoli e Bonus. Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il movimento degli animali quando vengono calpestati. Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

Dettagli Implementativi:
- Ostacoli:
Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7). Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso (chiave) ed i relaviti effetti (valore). Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.

- Bonus:
Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale di un numero determinato di quadrati (es: 5, 3, 10). I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso (chiave) ed i relaviti effetti (valore). Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.
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
bonus: dict = {5: 1, 15: 1, 25: 2, 35: 3, 45: 6, 55: 8}
ostacoli: dict = {10: -1, 20: -1, 30: -2, 40: -3, 50: -6, 60: -8}

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


def corsia_di_gara(race_track: list, rabbit: int, rabbit_stamina: int, tortoise: int, tortoise_stamina: int, weather: str, ostacoli: dict, bonus: dict, clock) -> str:
    
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

    # rabbit bonus / obstacle
    rabbit_pior_bonus_ostacoli = rabbit
    if rabbit_pior_bonus_ostacoli in bonus:
        rabbit += bonus[rabbit_pior_bonus_ostacoli]
        rabbit_ostacoli_bonus_sentence = f"Bonus in position {rabbit_pior_bonus_ostacoli}!!!"
    elif rabbit_pior_bonus_ostacoli in ostacoli:
        rabbit += ostacoli[rabbit_pior_bonus_ostacoli]
        rabbit_ostacoli_bonus_sentence = f"Obstacle in position {rabbit_pior_bonus_ostacoli}!!!"
    else:
        rabbit_ostacoli_bonus_sentence: str = "No bonus or obstacle!"

    # tortoise bonus / obstacle
    tortoise_pior_bonus_ostacoli = tortoise
    if tortoise_pior_bonus_ostacoli in bonus:
        tortoise += bonus[tortoise_pior_bonus_ostacoli]
        tortoise_ostacoli_bonus_sentence: str  = f"Bonus in position {tortoise_pior_bonus_ostacoli}!!!"
    elif tortoise_pior_bonus_ostacoli in ostacoli:
        tortoise += ostacoli[tortoise_pior_bonus_ostacoli]
        tortoise_ostacoli_bonus_sentence: str  = f"Obstacle in position {tortoise_pior_bonus_ostacoli}!!!"
    else:
        tortoise_ostacoli_bonus_sentence: str = "No bonus or obstacle!"

    # prints updated race track
    print("\n", "\n", " ".join(race_track), end="")
    print(f"\n rabbit stamina: {rabbit_stamina} || rabbit bonus or ostacle: {rabbit_ostacoli_bonus_sentence} || rabbit position: {rabbit}", end="")
    print(f"\n tortoise stamina: {tortoise_stamina} || tortoise bonus or ostacle: {tortoise_ostacoli_bonus_sentence} || tortoise position: {tortoise}", end="")
    print(f"\n weather: {weather} || elapsed time: {clock} sec", end="")
    
    # prints the winner and final clock
    if rabbit == 70 and tortoise == 70:
        print("")
        print("\n","IT'S A TIE.", end="")
        print("")
        print("\n", f"The race took {clock} seconds", end="")
    elif race_track[69] == "T":
        print("")
        print("\n","TORTOISE WINS! || VAY!!!", end="")
        print("")
        print("\n", f"The race took {clock} seconds")
    elif race_track[69] == "H":
        print("")
        print("\n","HARE WINS || YUCH!!!", end="")
        print("")
        print("\n", f"The race took {clock} seconds")


print("BANG !!!!! AND THEY'RE OFF !!!!!")


while race_track[69] == "_":
    corsia_di_gara(race_track, rabbit, rabbit_stamina, tortoise, tortoise_stamina, weather, ostacoli, bonus, clock)
    clock += 1
    weather = change_weather(weather, clock)
    rabbit, rabbit_stamina = rabbit_move(rabbit, rabbit_stamina, weather)
    tortoise, tortoise_stamina = tortoise_move(tortoise, tortoise_stamina, weather)