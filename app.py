from flask import Flask, render_template, request, redirect, session, url_for

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
app.secret_key = 'clave_secreta'

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
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')
    return render_template('index.html')


@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = request.form.get('nombre')
        userid = request.form.get('user_id')
        password = request.form.get('password')
        response = requests.get(API_URL + 'usuarios/'+userid)
        response.raise_for_status()
        usuario_base = response.json()

        if  (user for user in usuario_base if user[1] == password and user[5] == username):
            session['userid'] = userid
            return redirect(url_for('home'))
        else:
            return render_template('iniciar_sesion.html')



@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('home'))

@app.route('/dest')
def dest():
    
    return render_template('destination.html')


@app.route('/book')
def book():
        response = requests.get(API_URL + 'hoteles')
        response.raise_for_status()
        hoteles = response.json()

        response_img = requests.get(API_URL + 'img_hoteles')
        response_img.raise_for_status()
        imagenes = response_img.json()

        return render_template('booking.html', hoteles=hoteles, imagenes=imagenes)




@app.route('/habitaciones/<string:hotel>')
def habitaciones(hotel):
    
    return render_template('habitaciones.html', hotel=hotel)

@app.route('/book/<HotelID>')
def book_hotel(HotelID):

        response = requests.get(API_URL + 'hoteles/'+HotelID)
        response.raise_for_status()
        hotel = response.json()

        respuesta = requests.get(API_URL + 'tipos_de_habitacion')
        respuesta.raise_for_status()
        habitacion = respuesta.json()

        return render_template('reservar.html', hotel=hotel, habitacion=habitacion)




@app.route('/reservar/<string:hotel>/<string:habitacion>')
def reservar2(habitacion):
    
    return render_template('reservar.html', habitacion=habitacion)

@app.route('/reserva')
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

@app.route('/iniciar_sesion')
def iniciar_sesion():
    
    return render_template('iniciar_sesion.html')

@app.route('/packages')
def package():
    
    return render_template('package.html')

@app.route('/register')
def register():
    
    return render_template('register.html')

@app.route('/team')
def team():
    
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
