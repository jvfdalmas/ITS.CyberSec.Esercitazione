from flask import Flask, render_template, request

utente = ["mrossi@gmail.com", "RSSMRA10R40H501N", "1234", "0"]  # email, CFiscale, password, id_utente_dabase

app = Flask("__name__")

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/form-handler', methods=['GET'])
def handle_data():
    # Retrieve data from the GET request
    email = request.args.get('email')
    cfiscale = request.args.get('cfiscale')
    password = request.args.get('password')

    # Verify data and return appropriate response
    if email == utente[0] and cfiscale == utente[1] and password == utente[2]:
        return render_template('regiOK.html')
    else:
        return render_template('regiKO.html')

if __name__ == '__main__':
    app.run(host="192.168.0.200", port=8085)

