from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
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
        imagenes_json = response_img.json()
        imagenes_lista = list()
        for imagen in imagenes_json:
            if 'Img1.' in imagen['ImgHotel']:
                imagenes_lista.append(imagen)

        hoteles_imagenes = zip(hoteles, imagenes_lista)

        return render_template('booking.html', hoteles_imagenes=hoteles_imagenes)

@app.route('/book/<HotelID>')
def book_hotel(HotelID):

        response = requests.get(API_URL + 'hoteles/'+HotelID)
        response.raise_for_status()
        hotel = response.json()

        response_img_hoteles = requests.get(API_URL + 'img_hoteles')
        response_img_hoteles.raise_for_status()
        imagenes_hoteles_json = response_img_hoteles.json()
        imagenes_hoteles_filtradas = list()
        for imagen_hotel in imagenes_hoteles_json:
            if int(HotelID) == imagen_hotel['HotelID']:
                imagenes_hoteles_filtradas.append(imagen_hotel)

        hab_response = requests.get(API_URL + 'tipos_de_habitacion')
        hab_response.raise_for_status()
        habitacion = hab_response.json()
        habitaciones_filtradas = []
        HotelID = int(HotelID)
        for habit in habitacion:
            if habit['HotelID'] == HotelID:
                habitaciones_filtradas.append(habit)

        response_img_habitaciones = requests.get(API_URL + 'img_habitaciones')
        response_img_habitaciones.raise_for_status()
        imagenes_habitaciones_json = response_img_habitaciones.json()

        primer_tipoid = habitaciones_filtradas[0]['TipoID']
        ultimo_tipoid = habitaciones_filtradas[len(habitaciones_filtradas)-1]['TipoID']
        lista_tipos_de_habitacion = list(range(primer_tipoid, ultimo_tipoid+1))

        imagenes_habitaciones_filtradas = dict()

        for clave in lista_tipos_de_habitacion:
            imagenes_habitaciones_filtradas[clave] = []

        for imagen_habitacion in imagenes_habitaciones_json:
            if int(imagen_habitacion['TipoID']) in lista_tipos_de_habitacion:
                imagenes_habitaciones_filtradas[int(imagen_habitacion['TipoID'])].append(imagen_habitacion['ImgHabitacion'])


        return render_template('reservar.html', hotel=hotel, imagenes_hotel=imagenes_hoteles_filtradas, habitaciones=habitaciones_filtradas, imagenes_habitaciones=imagenes_habitaciones_filtradas)


@app.route('/habitaciones/<TipoID>')
def seleccion_habitacion(TipoID):

    response =requests.get(API_URL + '/habitaciones')
    response.raise_for_status()
    habitaciones = response.json()

    habitaciones_filtradas = []

    img_response = requests.get(API_URL + 'img_habitaciones')
    img_response.raise_for_status()
    imagen = img_response.json()

    TipoID = int(TipoID)
    for habit in habitaciones:
        if habit['TipoID'] == TipoID:
            habitaciones_filtradas.append(habit)

    habitacion_imagen = zip(habitaciones_filtradas, imagen)

    return render_template('seleccion_habitacion.html', habitacion_imagen=habitacion_imagen)

@app.route('/terminar_reserva/<HabitacionID>', methods=['GET', 'POST'])
def terminar_reserva(HabitacionID):
    if 'userid' not in session:
        return render_template('iniciar_sesion.html')

    formato_entrada = "%Y-%m-%dT%H:%M"
    formato_salida = "%Y-%m-%d %H:%M:%S"

    hora_actual = datetime.now()
    hora_actual_str = hora_actual.strftime(formato_salida)

    # Obtener las reservas no disponibles desde la API externa
    try:
        no_disp_response = requests.get(API_URL + 'reservas')
        no_disp_response.raise_for_status()
        no_disponibles = no_disp_response.json()
        reserva_id_max = max(reserva['ReservaID'] for reserva in no_disponibles)
        reserva_id_max = int(reserva_id_max)
        reserva_id_max = reserva_id_max + 1

    except requests.exceptions.RequestException as e:
        flash(f'Error al obtener las reservas: {e}', 'danger')
        return redirect(url_for('terminar_reserva', HabitacionID=HabitacionID))



    filtrado_no_disponibles = []
    HabitacionID = int(HabitacionID)
    for reserv in no_disponibles:
        if reserv['HabitacionID'] == HabitacionID:
            filtrado_no_disponibles.append(reserv)

    if request.method == 'POST':
        UsuarioID = session['userid']
        Desde_str = request.form.get('reserva_desde')
        Hasta_str = request.form.get('reserva_hasta')
        CantNiños = request.form.get('cantidad_de_niños')
        CantAdultos = request.form.get('cantidad_de_adultos')

        if not (Desde_str and Hasta_str and CantNiños and CantAdultos):
            flash('Todos los campos son obligatorios', 'danger')
            return redirect(url_for('terminar_reserva', HabitacionID=HabitacionID))

        PrecioTotal = (int(1) * int(CantAdultos)) + (int(1) * int(CantNiños))

        try:
            Desde_obj = datetime.strptime(Desde_str, formato_entrada)
            Desde_t = Desde_obj.strftime(formato_salida)
            Hasta_obj = datetime.strptime(Hasta_str, formato_entrada)
            Hasta_t = Hasta_obj.strftime(formato_salida)
        except ValueError:
            flash('Formato de fecha incorrecto', 'danger')
            return redirect(url_for('terminar_reserva', HabitacionID=HabitacionID))

        reserva = {
            'ReservaID': reserva_id_max,
            'Creacion': hora_actual_str,
            'Desde': Desde_t,
            'Hasta': Hasta_t,
            'CantNiños': int(CantNiños),
            'CantAdultos': int(CantAdultos),
            'PrecioTotal': PrecioTotal,
            'HabitacionID': HabitacionID,
            'UsuarioID': int(UsuarioID),
        }

        try:
            response = requests.post(API_URL + 'reservas', json=reserva)
            response.raise_for_status()
            flash('Reserva creada con éxito!', 'success')
            return redirect(url_for('reservas'))
        except requests.exceptions.RequestException as e:
            flash(f'Error al crear la reserva: {e}', 'danger')

    return render_template('terminar_reserva.html', filtrado_no_disponibles=filtrado_no_disponibles)


@app.route('/reserva')
def reservas():

    if 'userid' not in session:
        return render_template('iniciar_sesion.html')

    UsuarioID = session['userid']

    response = requests.get(API_URL + 'reservas')
    response.raise_for_status()
    reserva = response.json()
    mis_reservas = []
    UsuarioID = int(UsuarioID)
    for res in reserva:
        if res['UsuarioID'] == UsuarioID:
            mis_reservas.append(res)
    
    return render_template('reservas_act.html', reservas=mis_reservas)


@app.route('/cancelar_reserva/<ReservaID>', methods=['POST'])
def cancelar_reserva(ReservaID):
    if request.method == 'POST':
        try:
            response = requests.delete(API_URL+'reservas/'+ReservaID)
            response.raise_for_status()
            flash('Reserva cancelada con exito!')
            return redirect(url_for('reservas'))
        except requests.exceptions.RequestException as e:
            flash(f'error al cancelar la reserva: {e}')

        return render_template("ReservaCancelada.html")


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
