from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pricipal(): # funcion llamada principal mediante que se va a ejecutar lo que devuelve return
    return render_template("app_1_index.html") # aqui tenemos render_template que llama a index.html para realizar una llamada mediante la forma principal

@app.route("/variables") # dirrecion url que se agrega depues de la llamada al servidor
def variables():   # funcion llamada variable para llamarla 
    valor = "Antonio" # antonio es el valor que se le asigna a la variable valor
    valor_edad = 35  # una variable que contiene la edad
    return render_template("app_1_variables.html",nombre= valor, edad = valor_edad) 

if __name__ == '__main__':
    app.run(debug=True) 
    
    #Aqui las variables estan definidas en la app