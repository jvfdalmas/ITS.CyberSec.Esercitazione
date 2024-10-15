import requests, json, sys

base_url = "http://127.0.0.1:8080"


def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    return datiCittadino


def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")

check_login = False

def login():
    global username, password
    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    controlLogin()

def controlLogin():
    global check_login, sPriv
    jsonDataRequest = {"username": username, "password": password}
    response = requests.post(base_url + "/login", json=jsonDataRequest)
    if response.status_code == 200:
        data = response.json()
        print(data)
        check_login = True
        sPriv = data.get("Privilegi", "")
        return response.status_code, sPriv  
    else:
        print(f"Errore {response.status_code}: {response.text}")
        return response.status_code, None


print("Benvenuti al Comune - sede locale")

while not check_login:
    login()

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if iOper == 1:
        response_code, sPriv = controlLogin()
        if response_code == 200 and sPriv == "w":
            print("Aggiunta cittadino")
            api_url = base_url + "/add_cittadino"
            jsonDataRequest = GetDatiCittadino()
            EseguiOperazione(1, api_url, jsonDataRequest)
        else:
            print("Utente senza privilegi!")

    elif iOper == 2:
        response_code, sPriv = controlLogin()
        if response_code == 200 and (sPriv == "w" or sPriv == "r"):
            print("Richiesta dati cittadino")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = GetCodicefiscale()
            EseguiOperazione(2, api_url + "/" + jsonDataRequest['codFiscale'],None)
        else:
            print("Utente senza privilegi!")

    elif iOper == 3:
        response_code, sPriv = controlLogin()
        if response_code == 200 and sPriv == "w":
            print("Modifica cittadino")
            api_url = base_url + "/update_cittadino"
            jsonDataRequest = GetDatiCittadino()
            EseguiOperazione(3, api_url, jsonDataRequest)
        else:
            print("Utente senza privilegi!")


    elif iOper == 4:
        response_code, sPriv = controlLogin()
        if response_code == 200 and sPriv == "w":
            print("Eliminazione cittadino")
            api_url = base_url + "/elimina_cittadino"
            jsonDataRequest = GetCodicefiscale()
            EseguiOperazione(4, api_url, jsonDataRequest)
        else:
            print("Utente senza privilegi!")

    elif iOper == 5:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")




