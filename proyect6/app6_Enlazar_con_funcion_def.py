from flask import Flask, render_template

app = Flask(__name__)

@app.route("/enlace1")
def pagina3():
    return render_template("app_6_enlace1.html")

@app.route("/enlace2")
def pagina4():
    return render_template("app_6_enlace2.html")

if __name__ == '__main__':
    app.run(debug=True)