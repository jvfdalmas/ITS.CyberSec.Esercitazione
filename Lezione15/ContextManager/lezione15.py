print("\n", "\t","Lezione 15 - Esercizi Context Managers".upper(), "\n")

"""Esercizio 1 - Crea un context manager usando una classe. Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')"""

print("Soluzione - Esercizio 1:", "\n")

class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exec_type, exec_value, traceback):
        self.file.close()
        if exec_type is not None:   
            print(f"Execption type: {exec_type}")
            print(f"Execption type: {exec_value}")
            print(f"Execption type: {traceback}")


with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')
print(f.closed) # expected: True


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Esercizio 2 - Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1"""

print("Soluzione - Esercizio 2:", "\n")

from time import time, sleep

class Timer:

    def __init__(self):
        pass

    def __enter__(self):
        self.start = time()

    def __exit__(self, exec_type, exec_value, traceback):
        self.end = time()
        print(f"elapsed time: {self.end - self.start}")
        if exec_type is not None:   
            print(f"Execption type: {exec_type}")
            print(f"Execption type: {exec_value}")
            print(f"Execption type: {traceback}")

with Timer():
    sleep(1)