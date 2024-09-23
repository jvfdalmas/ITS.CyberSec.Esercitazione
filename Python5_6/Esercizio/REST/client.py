import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Suppress the InsecureRequestWarning from urllib3
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

    if istruzione == "1":
        nome = input("Inserire il nome: ")
        cognome = input("Inserire il cognome: ")
        cfiscale = input("Inserire il codice fiscale: ")
        dnascita = input("Inserire la data di nascita: ")
        data = [nome, cognome, cfiscale, dnascita]
        response = requests.post(app_url + "add_cittadini", json=data, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Authentiurllib3cation failed!")
        else:
            print(response.status_code, response.json())

    elif istruzione == "2":
        response = requests.get(app_url + "cittadini", verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Authentication failed!")
        else:
            print(response.status_code)
            for item in response.json():
                print(item)
                print("************")
    
    elif istruzione == "3":
        # Logic for modifying data (if needed)
        pass

    elif istruzione == "4":
        print("Inserire codice fiscale per eliminare cittadino: ")
        instr_del = input()
        # Assuming the server deletes based on CF
        data = {"cfiscale": instr_del}
        response = requests.post(app_url + "del_cittadini", json=data, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 401:
            print("Authentication failed!")
        else:
            print(response.status_code, response.json())

    elif istruzione == "5":
        AcquisiciCredenziali()
        response = requests.get(app_url + "authorization", verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            print("Autenticazione riuscita!")
        else:
            print("Autenticazione fallita!")

    elif istruzione == "6":
        flag = False
