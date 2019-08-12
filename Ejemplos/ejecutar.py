from flask import Flask
app = Flask(__name__)#nuevo Objeto
#Decorador
@app.route('/') 
def index():
    return "Hola Mundo desde Flask,Modo Debug"
#Cambiando otro puerto
#Actualizando cambios reflejados inmediatos
if __name__ == '__main__':
    app.run(debug = True ,port = 8000) #se encarga de ejecutar el servidor default puerto 5000