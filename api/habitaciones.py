from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

habitaciones_blueprint = Blueprint('habitaciones_blueprint', __name__)

QUERY_HABITACIONES = """
SELECT HabitacionID, HotelID, NumHabitacion, Piso, TipoDeHabitacion, CantHuespedes, Descripcion, Superficie, PrecioAdulto, PrecioNiño
FROM Habitaciones
"""

QUERY_HABITACION_BY_ID = """
SELECT HabitacionID, HotelID, NumHabitacion, Piso, TipoDeHabitacion, CantHuespedes, Descripcion, Superficie, PrecioAdulto, PrecioNiño
FROM Habitaciones
WHERE HabitacionID = :HabitacionID
"""

QUERY_HABITACION_ADD = """
INSERT INTO Habitaciones (HabitacionID, HotelID, NumHabitacion, Piso, TipoDeHabitacion, CantHuespedes, Descripcion, Superficie, PrecioAdulto, PrecioNiño)
VALUES (:HabitacionID, :HotelID, :NumHabitacion, :Piso, :TipoDeHabitacion, :CantHuespedes, :Descripcion, :Superficie, :PrecioAdulto, :PrecioNiño)
"""

QUERY_HABITACION_DELETE = """
DELETE FROM Habitaciones WHERE HabitacionID = :HabitacionID
"""
    
def habitaciones_all():
    return run_query(QUERY_HABITACIONES)

def habitacion_by_id(hab_id):
    return run_query(QUERY_HABITACION_BY_ID, {"HabitacionID": hab_id})

def habitacion_add(data):
    run_query(QUERY_HABITACION_ADD, data)

def habitacion_delete(hab_id):
    run_query(QUERY_HABITACION_DELETE, {'HabitacionID': hab_id})
    
@habitaciones_blueprint.route("/api/v1/habitaciones", methods=["GET"])
def get_habitaciones():
    try:
        result = habitaciones_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return(jsonify(result), 200)


@habitaciones_blueprint.route("/api/v1/habitaciones/<int:hab_id>", methods=["GET"])
def get_habitacion_by_id(hab_id):
    try:
        result = habitacion_by_id(hab_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@habitaciones_blueprint.route("/api/v1/habitaciones", methods=["POST"])
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


@habitaciones_blueprint.route('/api/v1/habitaciones/<int:hab_id>', methods=['DELETE'])
def delete_habitacion(hab_id):
    try:
        result = habitacion_by_id(hab_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró la reserva'}), 404

        habitacion_delete(hab_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (result,
        200,
    )