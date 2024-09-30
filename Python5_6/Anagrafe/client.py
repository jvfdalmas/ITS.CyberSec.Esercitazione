import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

flag = True
app_url = "https://127.0.0.1:8080/"
username = ""
password = ""

def StampaMenu():
    print("1. Inserire Dati")
    print("2. Stampare Dati")
    print("3. Modificare Dati")
    print("4. Eliminare Dati")
    print("5. Autenticazione")
    print("6. Exit")

def AcquisiciCredenziali():
    global username, password
    username = input("Inserisci username: ")
    password = input("Inserisci password: ")

while flag:
    StampaMenu()
    print("INSERIRE ISTRUZIONE:")
    istruzione = input()

    # commando per inserire cittadino
    if istruzione == "1": 
        nome = input("Inserire il nome: ")
        cognome = input("Inserire il cognome: ")
        cfiscale = input("Inserire il codice fiscale: ")
        dnascita = input("Inserire la data di nascita: ")
        data = {
            "nome": nome,
            "cognome": cognome,
            "cfiscale": cfiscale,
            "dnascita": dnascita
        }
        response = requests.post(app_url + "add_cittadini", json=data, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Autenticazione fallita!")
        elif response.status_code == 403:
            print("Utente non autorizato a inserire dato!")
        else:
            print(response.status_code, response.json())

    # commando per stampare cittadini
    elif istruzione == "2":
        response = requests.get(app_url + "cittadini", verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Autenticazione fallita!")
        else:
            print(response.status_code)
            for item in response.json():
                print(item)
    
    # commando per modificare cittadino
    elif istruzione == "3":
        print("Inserire codice fiscale per trovare il cittadino: ")
        cfiscale_id = input()
        print("Inserire il tipo di dato che vuoi cambiare: [nome] [cognome] [dnascita] [cfiscale]: ")
        tipo_dato = input()
        print("Inserire il dato nuovo: ")
        nuovo_dato = input()
        data = {"cfiscale_id": cfiscale_id, "tipo_dato": tipo_dato, "nuovo_dato": nuovo_dato}
        response = requests.post(app_url + "mod_cittadini", json=data, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Autenticazione fallita!")
        elif response.status_code == 403:
            print("Utente non autorizato a cambiare dati!")
        else:
            print(response.status_code, response.json())

    # commando per eliminare cittadino
    elif istruzione == "4":
        print("Inserire codice fiscale per eliminare cittadino per eliminarlo: ")
        instr_del = input()
        data = {"cfiscale": instr_del}
        response = requests.post(app_url + "del_cittadini", json=data, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Autenticazione fallita!")
        elif response.status_code == 403:
            print("Utente non autorizato a eliminare datto!")
        else:
            print(response.status_code, response.json())

    # commando per autenticazione dell'utente
    elif istruzione == "5":
        AcquisiciCredenziali()
        response = requests.get(app_url + "cittadini", verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            print("Autenticazione riuscita!")
        else:
            print("Autenticazione fallita!")

    # commando per uscire
    elif istruzione == "6":
        print("Arrivederci!")
        flag = False
