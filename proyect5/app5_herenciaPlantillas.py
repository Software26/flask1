from flask import Flask, render_template

app = Flask(__name__)

@app.route("/app_5_herencia_1")
def pagina1():
    return render_template("app_5_herencia_1.html")

@app.route("/app_5_herencia_2")
def pagina2():
    return render_template("app_5_herencia_2.html") #este es el enlce a la herecia 1.html

if __name__ == '__main__':
    app.run(debug=True)