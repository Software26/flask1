from flask import Flask, render_template # render_template es para enlazar las paguina web
from flask_wtf import FlaskForm #
from wtforms import StringField, SubmitField # esta es para importar los campos de caracteres o de texto, que son campos para formulario

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clavesecreta' # para poner los valores en secreto, esto es para temas de seguridad

class Formulario(FlaskForm):
    nombre = StringField("Nombre") #Etiqueta que aparece antes del texto
    enviar = SubmitField("Enviar") #Botton de texto para en enviar

@app.route('/', methods=['GET','POST']) #ruta principal con los metodos post y get
def principal():
    nombre = ''
    enviado = False
    formulario = Formulario() # esta es la instacia de la clase formulario que esta en la linea 9
    
    if formulario.validate_on_submit():
        enviado = True
        nombre = formulario.nombre.data
        formulario.nombre.data = ''

    return render_template('app_10_formulario.html',enviado=enviado,nombre=nombre,formulario=formulario)









if __name__ == '__main__':
    app.run(debug=True)


#Paquete que tiene las CLASES Y LIBRERIAS se instala con:
#pip install flask_WTF