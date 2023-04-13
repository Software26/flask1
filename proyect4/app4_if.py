from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def pricipal(): # funcion llamada principal mediante que se va a ejecutar lo que devuelve return
    return render_template("app_1_index.html") # aqui tenemos render_template que llama a index.html para realizar una llamada mediante la forma principal

@app.route("/frase/<texto>")
def frase(texto):
    return render_template("app_4_frase.html",tipo = texto)

if __name__ == '__main__':
    app.run(debug=True) 