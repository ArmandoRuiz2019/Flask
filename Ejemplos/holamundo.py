from flask import Flask
app = Flask(__name__)#nuevo Objeto
#Decorador
@app.route('/') 
def index():
    return "Hola Mundo desde Flask"
app.run() #se encarga de ejeuctar el servidor default puerto 5000
