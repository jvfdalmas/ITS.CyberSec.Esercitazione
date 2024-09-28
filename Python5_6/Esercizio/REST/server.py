from flask import Flask, request, jsonify
import base64

app = Flask("__name__")

cittadini = [
    {"nome": "Mario", "cognome": "Rossi", "cfiscale": "RSSMRA10R40H501N", "dnascita": "06/10/2010"},
    {"nome": "Giorgia", "cognome": "Rossella", "cfiscale": "GRRSS67R40H502S", "dnascita": "12/07/1967"},
    {"nome": "Alessia", "cognome": "Lacerda", "cfiscale": "ASSLCD40R40H502A", "dnascita": "09/01/1940"}
]

utenti = {"mario": "1234", "roberto": "5678"}

# funzione per verificare autenticazione
def is_authenticated():
    auth = request.headers.get('Authorization')
    if not auth:
        print("Authorization header missing")
        return False
    auth = auth[6:]
    security_data = base64.b64decode(auth).decode("utf-8")
    username, password = security_data.split(":")
    print(f"Username: {username}, Password: {password}")
    if username in utenti and utenti[username] == password:
        print("Authentication successful")
        return True
    print("Authentication failed")
    return False


# Route per aggiungere cittadino -- commando 1
@app.route('/add_cittadini', methods=['POST'])
def process_json():
    print("Received request to add citizen")
    
    if not is_authenticated():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json1 = request.json
        print(json1)
        cittadini.append(json1)
        return jsonify({"Esito": "ok", "Msg": "Dato inserito"}), 200
    else:
        return 'Content-Type not supported!', 400

# Route per stampare lista di cittadini -- commando 2
@app.route('/cittadini', methods=["GET"])
def get_cittadini():
    print("Received request to get citizens")

    if not is_authenticated():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    return jsonify(cittadini), 200


# Route per modificare cittadino -- commando 3
@app.route('/mod_cittadini', methods=['POST'])
def mod_cittadini():
    print("Received request to modify citizen")

    if not is_authenticated():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json1 = request.json
        print(json1)
        cf_id = json1.get("cfiscale_id")
        tipo_dato = json1.get("tipo_dato")
        nuovo_dato = json1.get("nuovo_dato")

        global cittadini
        cittadino_trovato = False

        for cittadino in cittadini:
            if cittadino["cfiscale"] == cf_id:
                cittadino[tipo_dato] = nuovo_dato
                cittadino_trovato = True
                break
        
        if cittadino_trovato:
            return jsonify({"Esito": "ok", "Msg": "Dato modificato"}), 200
        else:
            return jsonify({"Esito": "ok", "Msg": "Cittadino non trovato o campo inesistente"}), 404
        
    return 'Content-Type not supported!', 400


# Route per cancellare cittadino -- commando 4
@app.route('/del_cittadini', methods=['POST'])
def delete_cittadini():
    print("Received request to delete citizen")
    
    if not is_authenticated():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json1 = request.json
        print(json1)
        cf_to_delete = json1.get("cfiscale")
        
        global cittadini
        cittadino_trovato = False
        for cittadino in cittadini:
            if cittadino["cfiscale"] == cf_to_delete:
                cittadini.remove(cittadino)
                cittadino_trovato = True
                break
        
        if cittadino_trovato:
            return jsonify({"Esito": "ok", "Msg": "Cittadino eliminato"}), 200
        else:
            return jsonify({"Esito": "ok", "Msg": "Cittadino non trovato"}), 404
    return 'Content-Type not supported!', 400


# Route per autenticazione -- commando 5
@app.route('/authorization', methods=['GET'])
def check_auth():
    if not is_authenticated():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    return jsonify({"Esito": "ok", "Msg": "Authorized"}), 200


# Server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, ssl_context="adhoc")
