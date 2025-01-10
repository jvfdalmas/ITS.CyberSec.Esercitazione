from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Database - File JSON
users_file = "users.json"
vendita_file = "case_in_vendita.json"
affitto_file = "case_in_affitto.json"
vendite_casa_file = "vendite_casa.json"
affitti_casa_file = "affitti_casa.json"
filiali_file = "filiali.json"

# Caricare file JSON
def load_data(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Errore: Il file {file_path} contiene un JSON non valido.")
            return {}
    return {}

# Salvare dati su file JSON
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Inizializzazione dei database
users = load_data(users_file)
case_in_vendita = load_data(vendita_file)
case_in_affitto = load_data(affitto_file)
vendite_casa = load_data(vendite_casa_file)
affitti_casa = load_data(affitti_casa_file)
filiali = load_data(filiali_file)

# Controlla se il file utenti esiste e non è vuoto
if not users:
    print("Errore: Il file users.json è vuoto o non esiste.")
    exit(1)

for file_name in [vendita_file, affitto_file, vendite_casa_file, affitti_casa_file, filiali_file]:
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file, indent=4)

# Autenticazione utente
def authenticate_user():
    auth = request.authorization
    if not auth:
        return None, "Credenziali mancanti"
    username = auth.username
    password = auth.password
    user_data = users.get(username)
    if not user_data or user_data["password"] != password:
        return None, "Username o password non validi"
    return user_data, None

# Endpoint per testare il login
@app.route('/login', methods=['GET'])
def login_check():
    user, error = authenticate_user()
    if error:
        return jsonify({"error": error}), 403
    return jsonify({"message": "Login riuscito", "role": user["role"]})

# Cerca Casa Vendita
@app.route('/cerca_casa_vendita', methods=['GET'])
def cerca_casa_vendita():
    user, error = authenticate_user()
    if error or user["role"] != "agent":
        return jsonify({"error": "Accesso non autorizzato"}), 403

    metri_min = int(request.args.get('metri_min', 0))
    prezzo_max = float(request.args.get('prezzo_max', float('inf')))
    stato = request.args.get('stato', None)

    results = [
        casa for casa in case_in_vendita.values()
        if casa["metri"] >= metri_min and casa["prezzo"] <= prezzo_max and (stato is None or casa["stato"] == stato)
    ]
    return jsonify(results)

# Cerca Casa Affitto
@app.route('/cerca_casa_affitto', methods=['GET'])
def cerca_casa_affitto():
    user, error = authenticate_user()
    if error or user["role"] != "agent":
        return jsonify({"error": "Accesso non autorizzato"}), 403

    tipo_affitto = request.args.get('tipo_affitto', None)
    prezzo_max = float(request.args.get('prezzo_max', float('inf')))

    results = [
        casa for casa in case_in_affitto.values()
        if casa["prezzo_mensile"] <= prezzo_max and (tipo_affitto is None or casa["tipo_affitto"] == tipo_affitto)
    ]
    return jsonify(results)

# Report di Marketing
@app.route('/report_marketing', methods=['GET'])
def report_marketing():
    user, error = authenticate_user()
    if error or user["role"] != "marketing":
        return jsonify({"error": "Accesso non autorizzato"}), 403

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    vendite_report = [
        vendita for vendita in vendite_casa.values()
        if start_date <= vendita["data_vendita"] <= end_date
    ]
    affitti_report = [
        affitto for affitto in affitti_casa.values()
        if start_date <= affitto["data_affitto"] <= end_date
    ]

    guadagni_filiali = {}

    for vendita in vendite_report:
        proponente = vendita["filiale_proponente"]
        venditrice = vendita["filiale_venditrice"]
        prezzo = vendita["prezzo_vendita"]

        guadagni_filiali.setdefault(proponente, {"vendite": 0, "affitti": 0})
        guadagni_filiali[proponente]["vendite"] += prezzo * 0.03

        guadagni_filiali.setdefault(venditrice, {"vendite": 0, "affitti": 0})
        guadagni_filiali[venditrice]["vendite"] += prezzo * 0.01

    for affitto in affitti_report:
        venditrice = affitto["filiale_venditrice"]

        guadagni_filiali.setdefault(venditrice, {"vendite": 0, "affitti": 0})
        guadagni_filiali[venditrice]["affitti"] += 500

    report = {
        "vendite": vendite_report,
        "affitti": affitti_report,
        "guadagni_filiali": guadagni_filiali
    }

    return jsonify(report)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, ssl_context="adhoc")
