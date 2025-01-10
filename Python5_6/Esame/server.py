from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Database - File JSON
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
            print(f"Il file {file_path} non contiene un JSON valido. Verrà inizializzato a un dizionario vuoto.")
            return {}
    return {}

# Salvare dati su file JSON
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Inizializzazione dei database
case_in_vendita = load_data(vendita_file)
case_in_affitto = load_data(affitto_file)
vendite_casa = load_data(vendite_casa_file)
affitti_casa = load_data(affitti_casa_file)
filiali = load_data(filiali_file)

for file_name in [vendita_file, affitto_file, vendite_casa_file, affitti_casa_file, filiali_file]:
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file, indent=4)

# Cerca Casa Vendita
@app.route('/cerca_casa_vendita', methods=['GET'])
def cerca_casa_vendita():
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
    tipo_affitto = request.args.get('tipo_affitto', None)
    prezzo_max = float(request.args.get('prezzo_max', float('inf')))

    results = [
        casa for casa in case_in_affitto.values()
        if casa["prezzo_mensile"] <= prezzo_max and (tipo_affitto is None or casa["tipo_affitto"] == tipo_affitto)
    ]
    return jsonify(results)

# Registrare una casa venduta
@app.route('/venduta_casa', methods=['POST'])
def venduta_casa():
    data = request.get_json()
    catastale = data['catastale']

    casa_rimossa = None
    for key, casa in list(case_in_vendita.items()):
        if casa['catastale'] == catastale:
            casa_rimossa = case_in_vendita.pop(key)
            break

    if not casa_rimossa:
        return jsonify({"error": "Casa non trovata nel database delle case in vendita."}), 404

    save_data(vendita_file, case_in_vendita)

    nuova_vendita = {
        "catastale": data['catastale'],
        "data_vendita": data['data_vendita'],
        "filiale_proponente": data['filiale_proponente'],
        "filiale_venditrice": data['filiale_venditrice'],
        "prezzo_vendita": data['prezzo_vendita']
    }
    vendite_casa[len(vendite_casa) + 1] = nuova_vendita
    save_data(vendite_casa_file, vendite_casa)
    return jsonify({"message": "Casa venduta registrata con successo"})

# Registrare una casa affittata
@app.route('/affittata_casa', methods=['POST'])
def affittata_casa():
    data = request.get_json()
    catastale = data['catastale']

    casa_rimossa = None
    for key, casa in list(case_in_affitto.items()):
        if casa['catastale'] == catastale:
            casa_rimossa = case_in_affitto.pop(key)
            break

    if not casa_rimossa:
        return jsonify({"error": "Casa non trovata nel database delle case in affitto."}), 404

    save_data(affitto_file, case_in_affitto)

    nuovo_affitto = {
        "catastale": data['catastale'],
        "data_affitto": data['data_affitto'],
        "filiale_proponente": data['filiale_proponente'],
        "filiale_venditrice": data['filiale_venditrice'],
        "prezzo_affitto": data['prezzo_affitto'],
        "durata_contratto": data['durata_contratto']
    }
    affitti_casa[len(affitti_casa) + 1] = nuovo_affitto
    save_data(affitti_casa_file, affitti_casa)
    return jsonify({"message": "Casa affittata registrata con successo"})

# Report di Marketing
@app.route('/report_marketing', methods=['GET'])
def report_marketing():
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

# Cercare una filiale
@app.route('/cerca_filiale', methods=['GET'])
def cerca_filiale():
    nome = request.args.get('nome', None)

    if not nome:
        return jsonify({"error": "Nome della filiale non fornito."}), 400

    results = [
        filiale for filiale in filiali.values()
        if nome.lower() in filiale["nome"].lower()
    ]

    if not results:
        return jsonify({"message": "Nessuna filiale trovata con il nome fornito."}), 404

    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)