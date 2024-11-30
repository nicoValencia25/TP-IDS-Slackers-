from flask import Flask, render_template, request, redirect, session, url_for, flash
from sqlalchemy import except_

from api.habitaciones import habitaciones_blueprint
from api.hoteles import hoteles_blueprint
from api.img_habitaciones import img_habitaciones_blueprint
from api.img_hoteles import img_hoteles_blueprint
from api.reservas import reservas_blueprint
from api.servicios import servicios_blueprint
from api.servicios_contratados import servicios_contratados_blueprint
from api.tipos_de_habitacion import tipos_de_habitacion_blueprint
from api.usuarios import usuarios_blueprint
from datetime import datetime

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
    try:
        if  (user for user in usuario_base if user[1] == password and user[5] == username):
            session['userid'] = userid
            flash('sesion iniciada correctamente')
            return redirect(url_for('home'))
        else:
            flash(f'error al iniciar sesion')
            return redirect(url_for('home'))
    except requests.exceptions.RequestException as e:
        flash(f'error al crear la reserva: {e}')
        return render_template('404.html')



@app.route('/logout')
def logout():
    session.pop('userid', None)
    flash('logged out')
    return redirect(url_for('home'))

@app.route('/dest')
def dest():
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')
    
    return render_template('destination.html')


@app.route('/book')
def book():
        if 'userid' not in session:
            return render_template('iniciar_sesion.html')


        response = requests.get(API_URL + 'hoteles')
        response.raise_for_status()
        hoteles = response.json()

        response_img = requests.get(API_URL + 'img_hoteles')
        response_img.raise_for_status()
        imagenes = response_img.json()

        hoteles_imagenes = zip(hoteles, imagenes)

        return render_template('booking.html', hoteles_imagenes=hoteles_imagenes)

@app.route('/book/<HotelID>')
def book_hotel(HotelID):

        response = requests.get(API_URL + 'hoteles/'+HotelID)
        response.raise_for_status()
        hotel = response.json()

        img_response = requests.get(API_URL + 'img_hoteles/'+HotelID)
        img_response.raise_for_status()
        imagen = img_response.json()

        hab_response = requests.get(API_URL + 'tipos_de_habitacion')
        hab_response.raise_for_status()
        habitacion = hab_response.json()
        habitaciones_filtradas = [habit for habit in habitacion if habit['HotelID'] == HotelID]

        return render_template('reservar.html', hotel=hotel, imagen=imagen, habitacion=habitaciones_filtradas)


@app.route('/habitaciones/<TipoID>')  #aca falta verficiar q funciona
def seleccion_habitacion(TipoID):
    response =requests.get(API_URL + '/habitaciones'+TipoID)
    response.raise_for_status()
    habitaciones = response.json()

    img_response = requests.get(API_URL + 'img_habitaciones/'+TipoID)
    img_response.raise_for_status()
    imagen = img_response.json()

    habitacion_imagen = zip(habitaciones, imagen)

    return render_template('seleccion_habitacion.html', habitacion_imagen=habitacion_imagen)

@app.route('/terminar_reserva', methods=['GET','POST']) #aca se deberia finalizar la reserva mandando al back los datos que sean solicitados
def terminar_reserva(HabitacionID, PrecioAdulto):
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')

    no_disp_response = requests.get(API_URL + 'reservas') #voy a intentar usar un if para mostrar solo las de esa habitacion
    no_disp_response.raise_for_status()
    no_disponibles = no_disp_response.json()


    if request.method == 'POST':
        UsuarioID = session['userid']
        HabitacionID = HabitacionID
        Desde = request.form.get('reserva_desde')
        Hasta = request.form.get('reserva_hasta')
        CantNiños = request.form.get('cantidad_de_niños')
        CantAdultos = request.form.get('cantidad_de_adultos')
        Creacion = datetime.utcnow()
        PrecioTotal = (int(PrecioAdulto) * int(CantAdultos)) + ((int(PrecioAdulto)/2) * int(CantNiños))

        reserva = {
            'UsuarioID': UsuarioID,
            'HabitacionID': HabitacionID,
            'Desde': Desde,
            'Hasta': Hasta,
            'CantNiños': CantNiños,
            'CantAdultos': CantAdultos,
            'Creacion': Creacion.isoformat(),
            'PrecioTotal': PrecioTotal,
        }

        try:
            response = requests.post(url=f'{API_URL}/reservas', json=reserva)
            response.raise_for_status()  # Esto generará una excepción si la respuesta contiene un error HTTP
            flash('Reserva creada con exito!')
            return redirect(url_for('reserva'))
        except requests.exceptions.RequestException as e:
            flash(f'error al crear la reserva: {e}')

    return render_template('terminar_reserva.html',  no_disponibles = no_disponibles)

@app.route('/reserva')
def reservas():

    if 'userid' not in session:
        return render_template('iniciar_sesion.html')

    response = requests.get(API_URL + 'reservas')
    response.raise_for_status()
    reserva = response.json()
    
    return render_template('reservas_act.html', reserva=reserva)


@app.route('/reservas/<int:reserva_id>', methods=['DELETE'])
def cancelar_reserva(reserva_id):
    try:
        response = requests.delete(f'{API_URL}/reservas/{reserva_id}')
        response.raise_for_status()
        flash('Reserva cancelada con exito!')
    except requests.exceptions.RequestException as e:
        flash(f'error al cancelar la reserva: {e}')
    return redirect(url_for('reservas'))

@app.route('/sobre_nosotros')
def sobre_nosotros():
    
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')


    return render_template('contact.html')

@app.route('/packages')
def package():
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')
    
    return render_template('package.html')
@app.route('/team')
def team():
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')
    
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')
    
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
