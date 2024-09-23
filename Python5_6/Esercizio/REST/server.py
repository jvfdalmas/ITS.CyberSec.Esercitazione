from flask import Flask, request, jsonify
import base64

app = Flask("__name__")

# Sample data
cittadini = [
    ["Mario", "Rossi", "RSSMRA10R40H501N", "06/10/2010"],
    ["Giorgia", "Rossella", "GRRSS67R40H502S", "12/07/1967"],
    ["Alessia", "Lacerda", "ASSLCD40R40H502A", "09/01/1940"]
]

# Username: password dictionary
utenti = {"mario": "1234", "roberto": "5678"}

# Helper function to check if authentication is valid
@app.route('/authorization', methods=['POST'])
def check_auth():
    auth = request.headers.get('Authorization')
    if not auth:
        return False
    auth = auth[6:]  # Remove "Basic " prefix
    security_data = base64.b64decode(auth).decode("utf-8")
    username, password = security_data.split(":")
    # Check credentials
    if username in utenti and utenti[username] == password:
        return True
    return False

# Route to add a citizen
@app.route('/add_cittadini', methods=['POST'])
def process_json():
    print("Received request to add citizen")
    
    if not check_auth():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json1 = request.json
        print(json1)
        cittadini.append(json1)
        return jsonify({"Esito": "ok", "Msg": "Dato inserito"}), 200
    else:
        return 'Content-Type not supported!', 400

# Route to fetch all citizens
@app.route('/cittadini', methods=["GET"])
def get_cittadini():
    print("Received request to get citizens")
    
    if not check_auth():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    return jsonify(cittadini), 200

# Route to delete a citizen (this needs proper logic to delete citizens)
@app.route('/del_cittadini', methods=['POST'])
def delete_cittadini():
    print("Received request to delete citizen")
    
    if not check_auth():
        return jsonify({"Esito": "error", "Msg": "Unauthorized"}), 401
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json1 = request.json
        print(json1)
        # Add logic here to find and remove the citizen based on provided data (e.g., CF)
        return jsonify({"Esito": "ok", "Msg": "Dato eliminato"}), 200
    return 'Content-Type not supported!', 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, ssl_context="adhoc")
