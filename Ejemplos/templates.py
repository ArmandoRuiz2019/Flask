from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/usuario/<name>')
def user(name='Armando'):
    return render_template('index.html',nombre=name)

@app.route('/clientes')
def cliente():
    nombres = ['PEDRO','MIGUEL','RAUL']
    return render_template('clientes.html',lista =nombres)

if __name__ == '__main__':
    app.run(debug = True ,port = 8000) #se encarga de ejecutar el servidor