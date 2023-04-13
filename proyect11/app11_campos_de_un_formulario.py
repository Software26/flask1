from flask import Flask, render_template, url_for, redirect, session # render_template es para enlazar las paguina web
from flask_wtf import FlaskForm  
from wtforms import (StringField, SubmitField, BooleanField,DateTimeField,RadioField, SelectField,TextAreaField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'

class Formulario(FlaskForm):
    nombre = StringField('Nombre es', validators=[DataRequired()])
    edad = BooleanField('Eres mayor de edad')
    sexo = RadioField('Sexo:', choices=[('h','hombre'), ('m','mujer')])
    color = SelectField('Color favorito:', choices= [('Rojo','R'),('Verde','V'),('Azul','A')])
    
    comentario = TextAreaField()
    botton = SubmitField('Enviar')

@app.route("/informacion")
def informacion():
    return render_template('app_11_informacion.html')

@app.route('/datos', methods=['GET','POST'])
def datos():
    miformulario = Formulario()
    if miformulario.validate_on_submit(): # si formulario a sido enviado guarda la informacion que tiene en el objeto session
        session['nombre'] = miformulario.nombre.data
        session['edad'] = miformulario.edad.data
        session['sexo'] = miformulario.sexo.data
        session['color'] = miformulario.color.data
        session['comentario'] = miformulario.comentario.data
        session['botton'] = miformulario.botton
        return redirect(url_for('informacion'))
    
    return render_template('app_11_datos_formulario.html',formulario=miformulario)

if __name__=='__main__':
    app.run(debug=True)