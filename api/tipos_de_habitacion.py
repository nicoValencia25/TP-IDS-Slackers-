from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

tipos_de_habitacion_blueprint = Blueprint('tipos_de_habitacion_blueprint', __name__)

QUERY_TIPOS = """
SELECT TipoID, Nombre, CantHuespedes, Superficie, HotelID, Descripcion, PrecioAdulto, PrecioNiño
FROM TiposDeHabitacion
"""

QUERY_TIPO_BY_ID = """
SELECT TipoID, Nombre, CantHuespedes, Superficie, HotelID, Descripcion, PrecioAdulto, PrecioNiño
FROM TiposDeHabitacion
WHERE TipoID = :TipoID
"""

QUERY_TIPO_ADD = """
INSERT INTO TiposDeHabitacion (TipoID, Nombre, CantHuespedes, Superficie, HotelID, Descripcion, PrecioAdulto, PrecioNiño)
VALUES (:TipoID, :Nombre, :CantHuespedes, :Superficie, :HotelID, :Descripcion, :PrecioAdulto, :PrecioNiño)
"""

QUERY_TIPO_DELETE = """
DELETE FROM TiposDeHabitacion WHERE TipoID = :TipoID
"""


QUERY_TIPO_BY_HOTEL = """
SELECT TipoID, Nombre, CantHuespedes, Superficie, HotelID, Descripcion, PrecioAdulto, PrecioNiño
FROM TiposDeHabitacion
WHERE HotelID = :HotelID
"""
    
def tipos_all():
    return run_query(QUERY_TIPOS)

def tipo_by_id(tipo_id):
    return run_query(QUERY_TIPO_BY_ID, {"TipoID": tipo_id})

def tipo_add(data):
    run_query(QUERY_TIPO_ADD, data)

def tipo_delete(tipo_id):
    run_query(QUERY_TIPO_DELETE, {'TipoID': tipo_id})


def tipo_by_hotel(tipo_hotel_id):
    return run_query(QUERY_TIPO_BY_HOTEL, {"HotelID": tipo_hotel_id})
    
@tipos_de_habitacion_blueprint.route("/api/v1/tipos_de_habitacion", methods=["GET"])
def get_tipos():
    try:
        result = tipos_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200


@tipos_de_habitacion_blueprint.route("/api/v1/tipos_de_habitacion/<int:tipo_id>", methods=["GET"])
def get_tipo_by_id(tipo_id):
    try:
        result = tipo_by_id(tipo_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún tipo"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@tipos_de_habitacion_blueprint.route("/api/v1/tipos_de_habitacion", methods=["POST"])
def add_tipo():
    data = request.get_json()

    keys = (
        "TipoID",
        "Nombre",
        "CantHuespedes",
        "Superficie",
        "HotelID",
        "Descripcion",
        "PrecioAdulto",
        "PrecioNiño"
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = tipo_by_id(data["TipoID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un tipo con ese mismo ID"}), 400

        tipo_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@tipos_de_habitacion_blueprint.route('/api/v1/tipos_de_habitacion/<int:tipo_id>', methods=['DELETE'])
def delete_tipo(tipo_id):
    try:
        result = tipo_by_id(tipo_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el tipo'}), 404

        tipo_delete(tipo_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        result,
        200,
    )



@tipos_de_habitacion_blueprint.route("/api/v1/tipos_de_habitacion/<int:tipo_hotel_id>", methods=["GET"])
def get_tipo_by_hotel(tipo_hotel_id):
    try:
        result = tipo_by_hotel(tipo_hotel_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún tipo"}), 404

    result = result[0]
    return (
        result,
        200,
    )