from flask import Flask, render_template, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from db_utils.reservas import db, reservas_all, reserva_by_id, reserva_add, reserva_delete, habitaciones_all, habitacion_by_id, habitacion_add, habitacion_delete

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://juanbarbieri:Ei3_VskCP_nnnmT@juanbarbieri.mysql.pythonanywhere-services.com/juanbarbieri$HotelDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning from SQLAlchemy

db.init_app(app)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/vacaciones')
def provincias():
    
    return render_template('destination.html')

@app.route('/vacaciones/<string:provincia>')
def hoteles(provincia):

    return render_template('booking.html', provincia=provincia)

@app.route('/vacaciones/<string:provincia>/<string:hotel>')
def habitaciones(hotel):
    
    return render_template('habitaciones.html', hotel=hotel)

@app.route('/vacaciones/<string:provincia>/<string:hotel>/<string:habitacion>')
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

@app.route("/api/v1/reservas", methods=["GET"])
def get_reservas():
    try:
        result = reservas_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    response = []
    for row in result:
        response.append(
            jsonify(
                {
                    "ReservaID": row[0],
                    "ReservaCreacion": row[1],
                    "NumHabitacion": row[2],
                    "Hasta": row[3],
                    "CantNiños": row[4],
                    "CantAdultos": row[5],
                    "PrecioTotal": row[6],
                    "HabitacionID": row[7],
                    "UsuarioID": row[8],
                }
            )
        )

    return jsonify(response), 200


@app.route("/api/v1/reservas/<int:res_id>", methods=["GET"])
def get_reserva_by_id(res_id):
    try:
        result = reserva_by_id(res_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva"}), 404

    result = result[0]
    return (
        jsonify(
            {
                "ReservaID": result[0],
                "ReservaCreacion": result[1],
                "Desde": result[2],
                "Hasta": result[3],
                "CantNiños": result[4],
                "CantAdultos": result[5],
                "PrecioTotal": result[6],
                "HabitacionID": result[7],
                "UsuarioID": result[8],
            }
        ),
        200,
    )


@app.route("/api/v1/reservas", methods=["POST"])
def add_reserva():
    data = request.get_json()

    keys = (
        "ReservaID",
        "ReservaCreacion",
        "Desde",
        "Hasta",
        "CantNiños",
        "CantAdultos",
        "PrecioTotal",
        "HabitacionID",
        "UsuarioID",
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = reserva_by_id(data["ReservaID"])
        if len(result) > 0:
            return jsonify({"error": "Existe una reserva con ese mismo ID"}), 400

        reserva_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@app.route('/api/v1/reservas/<int:res_id>', methods=['DELETE'])
def delete_reserva(res_id):
    try:
        result = reserva_by_id(res_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró la reserva'}), 404

        reserva_delete(res_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        jsonify(
            {
                "ReservaID": res_id,
                "ReservaCreacion": result[1],
                "Desde": result[2],
                "Hasta": result[3],
                "CantNiños": result[4],
                "CantAdultos": result[5],
                "PrecioTotal": result[6],
                "HabitacionID": result[7],
                "UsuarioID": result[8],
            }
        ),
        200,
    )

@app.route("/api/v1/habitaciones", methods=["GET"])
def get_habitaciones():
    try:
        result = habitaciones_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    response = []
    for row in result:
        response.append(
            jsonify(
                {
                    "HabitacionID": row[0],
                    "HotelID": row[1],
                    "NumHabitacion": row[2],
                    "Piso": row[3],
                    "TipoDeHabitacion": row[4],
                    "CantHuespedes": row[5],
                    "Descripcion": row[6],
                    "Superficie": row[7],
                    "PrecioAdulto": row[8],
                    "PrecioNiño": row[9],
                }
            )
        )

    return jsonify(response), 200


@app.route("/api/v1/habitaciones/<int:hab_id>", methods=["GET"])
def get_habitacion_by_id(hab_id):
    try:
        result = habitacion_by_id(hab_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva"}), 404

    result = result[0]
    return (
        jsonify(
            {
                "HabitacionID": result[0],
                "HotelID": result[1],
                "NumHabitacion": result[2],
                "Piso": result[3],
                "TipoDeHabitacion": result[4],
                "CantHuespedes": result[5],
                "Descripcion": result[6],
                "Superficie": result[7],
                "PrecioAdulto": result[8],
                "PrecioNiño": result[9],
            }
        ),
        200,
    )


@app.route("/api/v1/habitaciones", methods=["POST"])
def add_habitacion():
    data = request.get_json()

    keys = (
        "HabitacionID",
        "HotelID",
        "NumHabitacion",
        "Piso",
        "TipoDeHabitacion",
        "CantHuespedes",
        "Descripcion",
        "Superficie",
        "PrecioAdulto",
        "PrecioNiño"
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = habitacion_by_id(data["HabitacionID"])
        if len(result) > 0:
            return jsonify({"error": "Existe una reserva con ese mismo ID"}), 400

        habitacion_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@app.route('/api/v1/habitaciones/<int:hab_id>', methods=['DELETE'])
def delete_habitacion(hab_id):
    try:
        result = habitacion_by_id(hab_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró la reserva'}), 404

        habitacion_delete(hab_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        jsonify(
            {
                "HabitacionID": hab_id,
                "HotelID": result[1],
                "NumHabitacion": result[2],
                "Piso": result[3],
                "TipoDeHabitacion": result[4],
                "CantHuespedes": result[5],
                "Descripcion": result[6],
                "Superficie": result[7],
                "PrecioAdulto": result[8],
                "PrecioNiño": result[9],
            }
        ),
        200,
    )

if __name__=='__main__':
    app.run(debug=True)