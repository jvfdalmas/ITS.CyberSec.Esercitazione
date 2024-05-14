"""" Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
- La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
- La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
"""

from random import choices

def turtle_race():
    turtle_steps:list = [3, -6, 1]
    turtle_steps_probability:list = [0.5, 0.2, 0.3]
    turtle_move = choices(turtle_steps, turtle_steps_probability)
    turtle_track_race:list = [numero for numero in range(1,71)]
    turtle_clock: int = 0
    turtle_track_race[0] = "turtle"
    tempo: str = "soleggiato"

    while turtle_track_race[69] != "turtle":
        
        turtle_move: list = choices(turtle_steps, turtle_steps_probability)
        turtle_move: int = int(turtle_move[0])

        last_index: int = turtle_track_race.index("turtle")
        turtle_track_race[last_index] = last_index + 1

        turtle_clock += 1
        
        if turtle_clock % 10 == 0:
            if tempo == "soleggiato":
                tempo = "pioggia"
            else:
                tempo = "soleggiato" 
        
        if tempo == "pioggia":
            turtle_move -= 1
            if last_index + turtle_move <= 0:
                turtle_track_race[0] = "turtle"
            if last_index + turtle_move >= 69:
                turtle_track_race[69] = "turtle"
            else:
                turtle_track_race[last_index + turtle_move] = "turtle"
        elif tempo == "soleggiato":
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
    tempo: str = "soleggiato"

    while rabbit_track_race[69] != "rabbit":
        
        rabbit_move: list = choices(rabbit_steps, rabbit_steps_probability)
        rabbit_move: int = int(rabbit_move[0])
        last_index: int = rabbit_track_race.index("rabbit")
        rabbit_track_race[last_index] = last_index + 1
        rabbit_clock += 1

        if rabbit_clock % 10 == 0:
            if tempo == "soleggiato":
                tempo = "pioggia"
            else:
                tempo = "soleggiato" 

        if tempo == "pioggia":
            rabbit_move -= 1            
            if last_index + rabbit_move <= 0:
                rabbit_track_race[0] = "rabbit"
            if last_index + rabbit_move >= 69:
                rabbit_track_race[69] = "rabbit"
            else:
                rabbit_track_race[last_index + rabbit_move] = "rabbit"
        else:
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






