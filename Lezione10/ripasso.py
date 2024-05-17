"""2. Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

For example:
Test 	Result
print(transform(4))
2
print(transform(-10))
-5"""

def transform(x:int) -> int:

    if x % 2 == 0:
        return x / 2
    else:
        return x * 3 - 1

"""3. Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.

For example:
Test 	Result
print(calcola_stipendio(40))
400.0
print(calcola_stipendio(0))
0.0"""

def calcola_stipendio(ore_lavorate: int) -> float:
    stipendio: float= 0
    
    if ore_lavorate <= 40:
        stipendio = 10.0 * ore_lavorate
        return stipendio
    else:
        stipendio = 400.0
        ore_lavorate -= 40
        stipendio = stipendio + ore_lavorate * (10.0 * 1.5)
        
    return stipendio

"""4. crivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51

For example:
Test 	Result
print_seq()
Sequenza a):
1
2
3
4
5
6
7
Sequenza b):
3
8
13
18
23
Sequenza c):
20
14
8
2
-4
-10

Sequenza d):
19
27
35
43
51"""

def print_seq(): 
    
    print("Sequenza a):")
    for a in range (1, 8):
        print(a)
    print()
    print("Sequenza b):")
    for b in range (3, 24, 5):
        print(b)
    print()
    print("Sequenza c):")
    for c in range (20, -11, -6):
        print(c)
    print()
    print("Sequenza d):")
    for d in range (19, 52, 8):
        print(d)
    
    return

print(print_seq())

"""5. Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!

For example:
Test 	Result
print(integerPower(3, 4))
81
print(integerPower(2, 5))
32"""

def integerPower(base: int, esponente: int) -> int:
    result = 1
    for _ in range(esponente):
        result *= base
    return result

print(integerPower(2, 5))

"""6. Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.
Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
For example:
Test 	Result
print(hypotenuse(3.0, 4.0))
5.0
print(hypotenuse(8.0, 15.0))
17.0"""

import math
def hypotenuse(lato1: float, lato2: float) -> float:
    hypotenusa_quadrato = lato1 ** 2 + lato2 ** 2
    hypotenusa = math.sqrt(hypotenusa_quadrato) 

    return hypotenusa

"""7. Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.

For example:
Test 	Result
print(convert_temperature(0))
32.0
print(convert_temperature(32, False))
0.0"""

def convert_temperature(temperature: float, to_fahrenheit: float = True):
    
    if to_fahrenheit == True:
        fahrenheit = 9/5*temperature + 32
        return fahrenheit
    else:
        celsius = 5/9 * (temperature -32)
        return celsius

"""8.  Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

For example:
Test 	Result
print(time_difference(1, 0, 0, 3, 15, 30))
8130
print(time_difference(0, 0, 0, 12, 0, 0))
43200"""

def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:
    ore_in_secondi = ore * 60 * 60
    minuti_in_secondi = minuti * 60
    secondi = secondi + ore_in_secondi + minuti_in_secondi
    return secondi

print(seconds_since_noon(3, 15, 50))

def time_difference(ore1: int, minuti1: int, secondi1: int, ore2: int, minuti2: int, secondi2: int) -> int:
    ore_in_secondi1: int = seconds_since_noon(ore1, minuti1, secondi1)
    ore_in_secondi2: int = seconds_since_noon(ore2, minuti2, secondi2)
    difference: int = ore_in_secondi1 - ore_in_secondi2
    if difference < 0:
        difference = - difference
    return difference

""" 9. Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!

Result
Tempo: 0 Altezza: 0.0
Tempo: 1 Altezza: 100.0
Tempo: 2 Altezza: 104.0
Tempo: 3 Altezza: 12.0
Tempo: 4 Rimbalzo!
Tempo: 5 Altezza: 88.0
Tempo: 6 Altezza: 230.0
Tempo: 7 Altezza: 276.0
Tempo: 8 Altezza: 226.0
Tempo: 9 Altezza: 80.0
Tempo: 10 Rimbalzo!
Tempo: 11 Altezza: 81.0
Tempo: 12 Altezza: 250.0
Tempo: 13 Altezza: 323.0
Tempo: 14 Altezza: 300.0
Tempo: 15 Altezza: 181.0
Tempo: 16 Rimbalzo!
Tempo: 17 Altezza: 17.0
Tempo: 18 Altezza: 172.5
Tempo: 19 Altezza: 232.0
Tempo: 20 Altezza: 195.5
Tempo: 21 Altezza: 63.0
Tempo: 22 Rimbalzo!
Tempo: 23 Altezza: 82.75
Tempo: 24 Altezza: 245.0
Tempo: 25 Altezza: 311.25
Tempo: 26 Altezza: 281.5
Tempo: 27 Altezza: 155.75
Tempo: 28 Rimbalzo!"""

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi != 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")
        tempo += 1

        if altezza >= 0:
            altezza = altezza + velocita
            velocita -= 96
            if altezza <= 0:
                rimbalzi += 1
                print(f"Tempo: {tempo} Rimbalzo!")
                altezza = altezza * -0.5
                velocita = velocita * -0.5
                tempo += 1

print(rimbalzo())

"""10. Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione, al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.
 
In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa, i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."

Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 

For example:
Test 	Result

memorizza_file([1100, 20000, 1048576, 512, 5000])

File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998.
File di 20000 byte compresso in 16000.0 byte e memorizzato. Blocchi usati: 31. Blocchi rimanenti: 967.
Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."""

def memorizza_file(files: list[int]) -> str:
    memorizzazione_disponibile = 1000

    for file in files:
        file_compresso = file * 0.8
        file_compresso_in_blocchi = math.ceil(file_compresso / 512)
        if file_compresso_in_blocchi <= memorizzazione_disponibile:
            memorizzazione_disponibile -= file_compresso_in_blocchi
            print(f"File di {file} byte compresso in {file_compresso} byte e memorizzato. Blocchi usati: {file_compresso_in_blocchi}. Blocchi rimanenti: {memorizzazione_disponibile}.")
        else:
            print(f"Non è possibile memorizzare il file di {file} byte. Spazio insufficiente..")
            break

print(memorizza_file([1100, 20000, 1048576, 512, 5000]))

