from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

API_URL = 'http://localhost:5000/api/v1/'
app = Flask(__name__)
app.secret_key = "clave_secreta"

users = {}
@app.route('/')
def home():
    return redirect(url_for('log'))

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = request.form.get('nombre')
        userlname = request.form.get('apellido')
        password = request.form.get('contraseña')
        email = request.form.get('email')
        if email in users and users[email] == password:
            session['user'] = email
            return redirect(url_for('index'))
        else:
            return redirect(url_for('log'))

    return render_template('iniciar_sesion.html')

@app.route('/dest')
def provincias():
    
    return render_template('destination.html')

@app.route('/book')
def hoteles():
        response = requests.get(API_URL + 'hoteles')
        response.raise_for_status()
        hoteles_all = response.json()
        return render_template('booking.html', hoteles=hoteles_all)

@app.route('/vacaciones/<string:provincia>/<string:hotel>')
def habitaciones(hotel):
    
    return render_template('habitaciones.html', hotel=hotel)

@app.route('/vacaciones/<string:provincia>/<string:hotel>/<string:habitacion>')
def reservar2(habitacion):
    
    return render_template('reservar2.html', habitacion=habitacion)

@app.route('/reservas/')
def reservas():
    
    return render_template('reservas_act.html')

@app.route('/reservas/<string:reserva>/editar_reserva')
def editar_reserva(reserva):
    
    return render_template('reservar.html', reserva=reserva)

@app.route('/reservas/<string:reserva>/cancelar_reserva')
def cancelar_reserva(reserva):
    
    return render_template('cancelar_reserva.html', reserva=reserva)

@app.route('/us')
def nosotros():
    
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
        niños = request.form.get('cantidad_de_niños')


    return render_template('reservar.html')

@app.route('/editar')
def reservar_editar():

    return render_template('editar_reserva.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/package')
def package():
    return render_template('package.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
