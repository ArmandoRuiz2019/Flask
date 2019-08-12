from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/usuario/<name>')
def user(name='Armando'):
    edad = 29
    cursos = ['PYTHON','FLASK','DJANGO']
    return render_template('usuario.html',nombre=name ,edad=edad,lista=cursos)

if __name__ == '__main__':
    app.run(debug = True ,port = 8000) #se encarga de ejecutar el servidor