import requests
import urllib3
import myjson

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sModel = "gemini-1.5-pro"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="

with open("GoogleAPIKey.txt","r") as file:
    GoogleAPIKey = file.read() 
    
api_url = base_url + GoogleAPIKey

# Accademia
with open("./Accademia/domains-tables.sql", "r") as file:
    sql_accademia = file.read()

# Cielo
with open("./Cielo/domains-tables.sql", "r") as file:
    sql_cielo = file.read()

print("SQL")

while True:
    print("\nOperazioni disponibili:")
    print("1. Accademia")
    print("2. Cielo")
    print("3. Esci")

    iOper = int(input("Cosa vuoi fare? "))

    if iOper == 1:
        sArgomento = input("Inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts": [{"text": "Ti verranno fornite informazioni su uno schema SQL, comprese tabelle e domini personalizzati definiti in PostgreSQL. Il tuo compito è generare query SQL valide per PostgreSQL che rispettino le seguenti caratteristiche: \n Usa i tipi di dati e i domini definiti nello schema. \n Rispetta i vincoli di dominio come check o not null. \n Non utilizzare funzioni non supportate da PostgreSQL. \n Rispondi sempre in italiano.\n" + sql_accademia + "Ecco la richiesta" + "\n" + sArgomento}]}]}
        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        if response.status_code==200:
            dResponse = response.json()
            dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
            print(sModel)
            print(dListaContenuti)

    elif iOper == 2:
        sArgomento = input("Inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts": [{"text": "Ti verranno fornite informazioni su uno schema SQL, comprese tabelle e domini personalizzati definiti in PostgreSQL. Il tuo compito è generare query SQL valide per PostgreSQL che rispettino le seguenti caratteristiche: \n Usa i tipi di dati e i domini definiti nello schema. \n Rispetta i vincoli di dominio come check o not null. \n Non utilizzare funzioni non supportate da PostgreSQL. \n Rispondi sempre in italiano.\n" + sql_cielo + "Ecco la richiesta" + "\n" + sArgomento}]}]}
        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        if response.status_code==200:
            dResponse = response.json()
            dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
            print(sModel)
            print(dListaContenuti)

 
    elif iOper == 3:
        print("Buona giornata!")
        break

    else:
        print("Operazione non disponibile, riprova.")
