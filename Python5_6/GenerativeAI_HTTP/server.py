from flask import Flask, render_template, request
import os
import requests
import subprocess
import myjson

api = Flask(__name__)

sModel = "gemini-1.5-flash-latest"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="
with open("GoogleAPIKey.txt","r") as file:
    GoogleAPIKey = file.read() 
api_url = base_url + GoogleAPIKey

def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["bash", "./creajsonpersf.sh"])
  subprocess.run(["rm", "./filericevuti/image.jpg"])

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/sendform', methods=['POST'])
def sendform():
    task = request.form.get('task')

    if task == "favola":
        if request.form.get("question"):
            sArgomento = request.form.get("question")
            jsonDataRequest = {"contents": [{"parts": [{"text": "voglio una favola che parla di " + sArgomento}]}]}
            response = requests.post(api_url,json=jsonDataRequest)
            if response.status_code==200:
                dResponse = response.json()
                dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
                return f"<HTML><BODY> {dListaContenuti} </BODY></HTML>"
        else:
            return "<HTML><BODY> Ti sei dimenticato di inserire la domanda! </BODY></HTML>"
    
    elif task == "domanda":
        if request.form.get("question"):
            sArgomento = request.form.get("question")
            jsonDataRequest = {"contents": [{"parts": [{"text": sArgomento}]}]}
            response = requests.post(api_url,json=jsonDataRequest)
            if response.status_code==200:
                dResponse = response.json()
                dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
                return f"<HTML><BODY> {dListaContenuti} </BODY></HTML>"
        else:
            return "<HTML><BODY> Ti sei dimenticato di inserire la domanda! </BODY></HTML>"
    
    else:
        if request.files.get('imageFile'):
            if request.form.get("question"):
                f = request.files['imageFile']
                f.save(os.path.join("filericevuti", "image.jpg"))
                ComponiJsonPerImmagine("./filericevuti/image.jpg")
                dJsonRequest = myjson.JsonDeserialize("request.json")
                sArgomento = request.form.get("question")
                dJsonRequest["contents"][0]["parts"][0]["text"] = sArgomento
                response = requests.post(api_url,json=dJsonRequest)
                if response.status_code==200:
                    dResponse = response.json()
                    dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"]
                    return f"<HTML><BODY> {dListaContenuti} </BODY></HTML>"
                else:
                    return f"<HTML><BODY> {response.status_code} </BODY></HTML>"
            else:
                return "<HTML><BODY> Ti sei dimenticato di inserire la domanda! </BODY></HTML>"
        else:
            return "<HTML><BODY> Ti sei dimenticato di inserire il file! </BODY></HTML>"

api.run(host="0.0.0.0",port=8085, ssl_context=("./certificates/01.pem", "./certificates/testkey.pem"))