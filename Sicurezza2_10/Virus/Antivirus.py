#!/usr/bin/env python3
import os
import time
import psutil

def get_running_processes():
    """
    Ottiene un dizionario di processi attualmente in esecuzione.
    Chiave: PID, Valore: Nome del processo
    """
    processes = {}
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes[proc.info['pid']] = proc.info['name']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def kill_process(pid):
    """
    Tenta di terminare un processo dato il suo PID.
    Prima prova con SIGTERM, poi con SIGKILL se necessario.
    """
    try:
        process = psutil.Process(pid)
        process_name = process.name()
        
        print(f"Tentativo di terminare il processo {process_name} (PID: {pid}) con SIGTERM...")
        process.terminate()
        
        # Aspetta fino a 3 secondi per vedere se il processo termina
        gone, alive = psutil.wait_procs([process], timeout=3)
        if process in alive:
            print(f"Il processo {process_name} non risponde a SIGTERM. Uso SIGKILL...")
            process.kill()
        
        print(f"Processo {process_name} (PID: {pid}) terminato con successo.")
        return True
    except psutil.NoSuchProcess:
        print(f"Il processo con PID {pid} non esiste più.")
        return True
    except Exception as e:
        print(f"Errore durante il tentativo di terminare il processo {pid}: {e}")
        return False

def kill_all_with_name(name):
    """
    Termina tutti i processi con un dato nome.
    Restituisce il numero di processi terminati.
    """
    count = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == name:
                if kill_process(proc.info['pid']):
                    count += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return count

def main():
    print("Monitor di Processi - Rileva e termina nuovi processi")
    print("Acquisizione processi iniziali in esecuzione...")
    
    # Ottieni i processi iniziali
    initial_processes = get_running_processes()
    print(f"Rilevati {len(initial_processes)} processi in esecuzione.")
    
    print(f"Attendo 30 secondi per rilevare nuovi processi...")
    time.sleep(30)
    
    # Ottieni i processi dopo l'attesa
    current_processes = get_running_processes()
    print(f"Rilevati {len(current_processes)} processi in esecuzione dopo l'attesa.")
    
    # Trova nuovi processi
    new_processes = {}
    for pid, name in current_processes.items():
        if pid not in initial_processes:
            new_processes[pid] = name
    
    # Mostra e gestisci i nuovi processi
    if new_processes:
        print(f"\nRilevati {len(new_processes)} nuovi processi:")
        for pid, name in new_processes.items():
            print(f"PID: {pid} - Nome: {name}")
            
            response = input(f"Vuoi terminare il processo '{name}' (PID: {pid}) e tutti i processi con lo stesso nome? (s/n): ")
            if response.lower() in ['s', 'si', 'sì', 'y', 'yes']:
                # Termina tutti i processi con lo stesso nome
                count = kill_all_with_name(name)
                print(f"Terminati {count} processi con nome '{name}'.")
            else:
                print(f"Processo {name} ignorato.")
    else:
        print("\nNessun nuovo processo rilevato nell'intervallo di 60 secondi.")
    
    print("\nMonitoraggio terminato.")

if __name__ == "__main__":
    # Verifica se l'utente ha i privilegi necessari per terminare processi
    if os.geteuid() != 0:
        print("Avviso: Questo script potrebbe richiedere privilegi di amministratore per terminare alcuni processi.")
        print("Si consiglia di eseguirlo con 'sudo' per avere accesso completo.")
        response = input("Vuoi continuare senza privilegi di amministratore? (s/n): ")
        if response.lower() not in ['s', 'si', 'sì', 'y', 'yes']:
            print("Script terminato. Eseguilo con 'sudo python3 script.py' per avere i privilegi necessari.")
            exit(1)
    
    main()