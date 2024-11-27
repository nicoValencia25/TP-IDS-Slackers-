from flask import Flask, render_template, request, redirect

from api.habitaciones import habitaciones_blueprint
from api.hoteles import hoteles_blueprint
from api.img_habitaciones import img_habitaciones_blueprint
from api.img_hoteles import img_hoteles_blueprint
from api.reservas import reservas_blueprint
from api.servicios import servicios_blueprint
from api.servicios_contratados import servicios_contratados_blueprint
from api.tipos_de_habitacion import tipos_de_habitacion_blueprint
from api.usuarios import usuarios_blueprint

import requests

API_URL = 'https://juanbarbieri.pythonanywhere.com/api/v1/'

app = Flask(__name__)

app.register_blueprint(habitaciones_blueprint)
app.register_blueprint(hoteles_blueprint)
app.register_blueprint(img_habitaciones_blueprint)
app.register_blueprint(img_hoteles_blueprint)
app.register_blueprint(reservas_blueprint)
app.register_blueprint(servicios_blueprint)
app.register_blueprint(servicios_contratados_blueprint)
app.register_blueprint(tipos_de_habitacion_blueprint)
app.register_blueprint(usuarios_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = request.form.get('nombre')
        userlname = request.form.get('apellido')
        password = request.form.get('contraseña')
        email = request.form.get('email')
        if email in users and users[email] == password:
            session['user'] = email
            return redirect('index')
        else:
            error_message= "Usuario o contraseña incorrectos. Por favor, vuelta a intentarlo."
            return render_template('error.html', error= error_message)

    return render_template('iniciar_sesion.html')

@app.route('/dest')
def dest():
    
    return render_template('destination.html')


@app.route('/book')
def book():
        response = requests.get(API_URL + 'hoteles')
        response.raise_for_status()
        hoteles = response.json()
        return render_template('booking.html', hoteles=hoteles)


@app.route('/habitaciones/<string:hotel>')
def habitaciones(hotel):
    
    return render_template('habitaciones.html', hotel=hotel)

@app.route('/reservar/<string:hotel>/<string:habitacion>')
def reservar(habitacion):
    
    return render_template('reservar.html', habitacion=habitacion)

@app.route('/reservas')
def reservas():
    
    return render_template('reservas_act.html')

@app.route('/reservas/<string:reserva>/editar_reserva')
def editar_reserva(reserva):
    
    return render_template('editar_reserva.html', reserva=reserva)

@app.route('/reservas/<string:reserva>/cancelar_reserva')
def cancelar_reserva(reserva):
    
    return render_template('cancelar_reserva.html', reserva=reserva)

@app.route('/sobre_nosotros')
def sobre_nosotros():
    
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    
    return render_template('contact.html')


@app.route('/reservar')
def reservar_hotel():
    if request.method == 'POST':
        inicio = request.form.get('reserva_desde')
        fin = request.form.get('reserva_hasta')
        habitacion_id = request.form.get('habitacion_id')
        adultos = request.form.get('cantidad_de_adultos')
        ninos = request.form.get('cantidad_de_ninos')


@app.route('/iniciar_sesion')
def iniciar_sesion():
    
    return render_template('iniciar_sesion.html')

@app.route('/packages')
def packages():
    
    return render_template('packages.html')

@app.route('/register')
def register():
    
    return render_template('register.html')

@app.route('/services')
def services():
    
    return render_template('services.html')

@app.route('/team')
def team():
    
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
