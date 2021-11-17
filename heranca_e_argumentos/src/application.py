from flask import app, Flask, render_template

minha_app = Flask(__name__)

@minha_app.route('/')
def home():
    return render_template('home.html')


@minha_app.route('/personalizada')
def home_perso():
    usu = 'Fabrício'
    return render_template('home_personalizada.html', usuario=usu)

if __name__ == '__main__':
    minha_app.run('0.0.0.0')