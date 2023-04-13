from flask import Flask, render_template,flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'

class Formulario(FlaskForm):
    botton = SubmitField("Enviar mesaje")

@app.route("/mensaje", methods=['GET','POST'])
def mensaje():
    formulario = Formulario()
    if formulario.validate_on_submit():
        flash("Gracias por pulsar este boton")
        return redirect(url_for('mensaje'))
    return render_template("app_12_error.html",formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)
    