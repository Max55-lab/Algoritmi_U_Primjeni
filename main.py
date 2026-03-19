from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')#Korijenski link ili glavni korijen
def home():
    return "Hello World!"


@app.route('/kontakt')#Kontatk link
def contat():
    return "Hello my contat info is ***!"



@app.route('/e-mail')#Kontatk link email
def mail():
    return "Hello my e-mail info is no.thank@gmail.com!"

@app.route('/pozdrav/<ime>')#Kontatk link za ime, NE KORISTIMO ZA OSLJETIVE INFORAMICE IME PERZIME LOZINKA, itd
def pozdrav(ime):
    return "Hello:"+ime

@app.route('/pozdrav/<prezime>/<ime>')
def ime_prezime(prezime, ime):
    return f"Hello:{prezime},{ime}"
@app.route('/zbroji/<int:broj1>/<int:broj2>')#pazi na poziv brojeva  treba savitt int definicju
def zbroji(broj1, broj2):
    return f" Suma je: {broj1+broj2}"

@app.route('/prijava')
def prijava():
    korisnicko_ime=request.args.get('kor_ime')
    lozinka = request.args.get('lozinka')
    if korisnicko_ime=='Marko' and lozinka=='123':
        return "Dobrodosao Marko"
    else:
        return "Netocni pristupni podaci"

#Sto treba unijet pri prijavi:prijava?kor_ime=unos&lozinka=unos#

@app.route('/app_info')
def jsoninfy():
    # Kreiramo rječnik (dictionary) s podacima
    podaci = {
        "kolegij": "Algoritmi u primjeni",
        "godina": 2026,
        "status": "aktivan"
    }
    # jsonify pretvara taj rječnik u format koji browser razumije
    return jsonify(podaci)

@app.route('/html')
def html():
    return 'Dobar dan.<p>Ovo je paragarf</p>'+ 'Ovo je link <a href="https://liveexample.pearsoncmg.com/liang/py/">Klikni ovdje za Liang Python primjere</a>'


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/pomnozi', methods=['POST'])
def pomnozi():
    data = request.get_json()

    # Dohvaćanje podataka (dobra praksa je postaviti default vrijednost na 0 ili None)
    broj1 = data.get("broj1", 0)
    broj2 = data.get("broj2", 0)

    # Izračun
    umnozak = broj1 * broj2

    # Popravljena sintaksa za rječnik (nedostajao je navodnik i zarez)
    return jsonify({
        "umnozak": umnozak
    })

#Zadatak 3
#Naprravi POST rutu koja ujedno prima i jedan argument kroz url
#Kroz boddy slaju dva argumenta
#Npr. kroz url saljemo JMBG,a kroz body saljemo ime i prezime
#Sa JSON-om vracamonatrag sa tre podatka

@app.route('/html/<jmbg>/',methods=['POST'])
def zadatak(jmbg):
    data = request.get_json()
    ime=data.get("ime")
    prezime=data.get("prezime")

    return jsonify({
        "ime":ime,
        "prezime":prezime,
        "jmbg":jmbg
    })

if __name__ == '__main__':
    app.run(debug=True)

