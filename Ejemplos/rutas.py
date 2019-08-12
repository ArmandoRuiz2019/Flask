from flask import Flask
from flask import request
app = Flask(__name__)#nuevo Objeto

#Decorador
@app.route('/') 
def index():
    return "Hola Mundo desde Flask,Modo Debug"

@app.route('/clientes') 
def clientes():
    return "Zona de Clientes"

@app.route('/usuarios') 
def usuarios():
    param = request.args.get('usuario','Campo usuario vacio')
    param2 = request.args.get('clave','Campo clave vacio')
    return "El Usuario es :{},{}".format(param,param2)



#Cambiando otro puerto
#Actualizando cambios reflejados inmediatos
if __name__ == '__main__':
    app.run(debug = True ,port = 8000) #se encarga de ejecutar el servidor default puerto 5000
