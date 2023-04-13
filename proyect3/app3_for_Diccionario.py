from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def pricipal(): # funcion llamada principal mediante que se va a ejecutar lo que devuelve return
    return render_template("app_1_index.html") # aqui tenemos render_template que llama a index.html para realizar una llamada mediante la forma principal


@app.route("/colores")
def colores():
    lista_colores = ["Verde","Rojo","Amarillo","Azul"]
    return render_template("app_3_for_colores.html", colores = lista_colores)


if __name__ == '__main__':
    app.run(debug=True) 