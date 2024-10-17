import requests
import subprocess
import urllib3
import myjson

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
GoogleAPIKey = "AIzaSyAcK5-_Ermfo4biwauu6irQEB9yqdSiMnk" # not active
api_url = base_url + GoogleAPIKey

def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./image.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath,"./image.jpg"])
  subprocess.run(["bash", "./creajsonpersf.sh"])

print("Benvenuti nella mia Generativa AI")

while True:
    print("\nOperazioni disponibili:")
    print("1. Creare una favola")
    print("2. Rispondere ad una domanda")
    print("3. Rispondere ad una domanda su un file img")
    print("4. Esci")

    iOper = int(input("Cosa vuoi fare? "))

    if iOper == 1:
        sArgomento = input("Inserisci l'argomento della favola: ")
        jsonDataRequest = {"contents": [{"parts": [{"text": "voglio una favola che parla di " + sArgomento}]}]}
        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        if response.status_code==200:
            dResponse = response.json()
            dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
            print(dListaContenuti)

    elif iOper == 2:
        sArgomento = input("Fai una domanda: ")
        jsonDataRequest = {"contents": [{"parts": [{"text": sArgomento}]}]}
        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        if response.status_code==200:
            dResponse = response.json()
            dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
            print(dListaContenuti)

    elif iOper == 3:
        sFile = input("Inserisce il path completo del file img: ")
        ComponiJsonPerImmagine(sFile)
        dJsonRequest = myjson.JsonDeserialize("request.json")
        sArgomento = input("Fai una domanda: ")
        dJsonRequest["contents"][0]["parts"][0]["text"] = sArgomento
        response = requests.post(api_url,json=dJsonRequest,verify=False)
        if response.status_code==200:
            dResponse = response.json()
            dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
            print(dListaContenuti)
        else:
            print(response.status_code)
 
    elif iOper == 4:
        print("Buona giornata!")
        break

    else:
        print("Operazione non disponibile, riprova.")
