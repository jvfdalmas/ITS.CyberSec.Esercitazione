#!/usr/bin/env python3
import os, sys, time
from setproctitle import setproctitle
import threading
from math import log as ln

def sieve_of_eratosthenes(limit):
    """Generate all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm."""
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

def read_integer(prompt):
    """Read an integer from input and check for errors."""
    while True:
        try:
            return int(input(prompt)) % 100000
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_first_n_primes(n): 
    """Print the first n prime numbers."""
    limit = int(2*n*(ln(n)-ln(ln(n))))
    primes = sieve_of_eratosthenes(limit)
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)
    for prime in primes[:n]:
        print(prime, end=', ')
    print()

def daemonize():
    """Detach process and run as daemon."""
    try:
        pid = os.fork() # Il primo fork() crea un processo figlio. Una copia identica. 
        if pid > 0: #  If the result of os.fork() = zero, then you're working in the child. Otherwise, you're working in the parent, and the return value is the PID (Process IDentifier) of the child.
            n = read_integer("Inserire quanti numeri primi vuoi generare: ")
            print_first_n_primes(int(n)) # Nel processo genitore, chiede quanti numeri primi generare e poi termina
            sys.exit(0)
    except OSError as e:
        sys.stderr.write("Fork #1 failed: {}\n".format(e))
        sys.exit(1)
    os.chdir("/")
    os.setsid() # crea una nuova sessione con setsid() e imposta i permessi
    os.umask(0)
    try:
        pid = os.fork() # Un secondo fork() crea un altro processo figlio completamente distaccato
        if pid > 0: #  If the result of os.fork() = zero, then you're working in the child.
            sys.exit(0)
    except OSError as e:
        sys.stderr.write("Fork #2 failed: {}\n".format(e))
        sys.exit(1)
    sys.stdout.flush() # Reindirizza stdin, stdout e stderr a /dev/null per nascondere output
    sys.stderr.flush()
    with open('/dev/null', 'r') as read_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'a+') as write_null:
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())

def replicate(target_dir, script):  # Questa funzione simula la replicazione del virus:
    """Simulate virus replication by copying the script and logging the event."""
    if not os.path.exists(target_dir): # Crea una directory target se non esiste
        os.makedirs(target_dir)
    destination = os.path.join(target_dir, os.path.basename(script))
    print(f"Replicating {script} to {destination}")
    with open(script, 'r') as src:
        content = src.read()  # Copia il codice sorgent
    with open(destination, 'w') as dst: # Incolla il codice sorgente in questa directory
        dst.write(content)
    with open(os.path.join(target_dir, "replication.log"), "a") as log: # Registra l'evento di replicazione in un file di log
        log.write(f"Replicated at {time.ctime()}\n")

def scan_files(directory, target_dir): # Simula l'esplorazione del filesystem:
    """Scan all files in the given directory and print their names."""
    try:
        while True:
            for root, dirs, files in os.walk(directory): # Scansiona ricorsivamente una directory
                for file in files:
                    size = os.path.getsize(os.path.join(root, file))
                    with open(os.path.join(target_dir, "files.log"), "a") as log:
                        log.write(f"Found file {os.path.join(root, file)} of size: {size}\n") # Registra i file trovati e le loro dimensioni in un file di log
                    #print(f"Found file {os.path.join(root, file)} of size: {size}\n")
                    time.sleep(3)
    except Exception as e:
        with open(os.path.join(target_dir, "files.log"), "a") as log:
            log.write(f"Error: {e}\n")
        time.sleep(5)

if __name__ == '__main__':
    # Change the process title for identification in the process list
    print("Running virus")
    setproctitle("MyDaemonVirus")

    # takes folder names
    script = sys.argv[0]
    script = os.path.abspath(script)
    current_folder = os.path.dirname(script)
    print(f"Current folder: {current_folder}")
    print(f"Script: {script}")
    target_dir = current_folder+"/virus_simulation"
    print(f"Target directory: {target_dir}")

    #Scan home folder
    home_directory = os.path.expanduser("~")

    # Daemonize the process so it runs in the background
    print("Daemonizing process")
    daemonize() # Chiama daemonize() per eseguirsi in background

    # Run scan_files in a separate thread
    scan_thread = threading.Thread(target=scan_files, args=(home_directory, target_dir)) # Avvia un thread separato per eseguire scan_files sulla home directory
    scan_thread.start()

    # Run replication every 60 seconds indefinitely
    while True: # Entra in un ciclo infinito dove continuerà finché il processo non viene terminato manualmente
        print("Replicating")
        replicate(target_dir, script)
        time.sleep(10) # Replica sé stesso ogni 10 secondi 

# Non esiste una relazione di dipendenza diretta tra le funzioni replicate e scan_files nel codice. Sono due funzionalità distinte che simulano comportamenti diversi di un malware e vengono eseguite indipendentemente l'una dall'altra.scan_files viene avviato in un thread separato. replicate viene eseguito ciclicamente nel thread principale.
