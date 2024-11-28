from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

hoteles_blueprint = Blueprint('hoteles_blueprint', __name__)

QUERY_HOTELES = """
SELECT HotelID, Nombre, Provincia, Descripcion, Direccion, CodigoPostal, Localidad, Longitud, Latitud
FROM Hoteles
"""

QUERY_HOTEL_BY_ID = """
SELECT HotelID, Nombre, Provincia, Descripcion, Direccion, CodigoPostal, Localidad, Longitud, Latitud
FROM Hoteles
WHERE HotelID = :HotelID
"""

QUERY_HOTEL_ADD = """
INSERT INTO Hoteles (HotelID, Nombre, Provincia, Descripcion, Direccion, CodigoPostal, Localidad, Longitud, Latitud)
VALUES (:HotelID, :Nombre, :Provincia, :HotelID, :Descripcion, :Direccion, :CodigoPostal, :Localidad, :Longitud, :Latitud)
"""

QUERY_HOTEL_DELETE = """
DELETE FROM Hoteles WHERE HotelID = :HotelID
"""

QUERY_HOTELID_BY_HABID = """
SELECT HotelID
FROM TiposDeHabitacion
INNER JOIN Habitaciones on Habitaciones.TipoID = TiposDeHabitacion.TipoID
WHERE HabitacionID = :HabitacionID
"""

def hoteles_all():
    return run_query(QUERY_HOTELES)

def hotel_by_id(hotel_id):
    return run_query(QUERY_HOTEL_BY_ID, {"HotelID": hotel_id})

def hotel_add(data):
    run_query(QUERY_HOTEL_ADD, data)

def hotel_delete(hotel_id):
    run_query(QUERY_HOTEL_DELETE, {'HotelID': hotel_id})

def hotel_by_habid(hab_id):
    return run_query(QUERY_HOTELID_BY_HABID, {"HabitacionID": hab_id})

@hoteles_blueprint.route("/api/v1/hoteles", methods=["GET"])
def get_hoteles():
    try:
        result = hoteles_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200


@hoteles_blueprint.route("/api/v1/hoteles/<int:hotel_id>", methods=["GET"])
def get_hotel_by_id(hotel_id):
    try:
        result = hotel_by_id(hotel_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún hotel"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@hoteles_blueprint.route("/api/v1/hoteles", methods=["POST"])
def add_hotel():
    data = request.get_json()

    keys = (
        "HotelID",
        "Nombre",
        "Provincia",
        "HotelID",
        "Descripcion",
        "Direccion",
        "CodigoPostal",
        "Localidad",
        "Longitud",
        "Latitud"
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = hotel_by_id(data["HotelID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un hotel con ese mismo ID"}), 400

        hotel_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@hoteles_blueprint.route('/api/v1/hoteles/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    try:
        result = hotel_by_id(hotel_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el hotel'}), 404

        hotel_delete(hotel_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        result,
        200,
    )

@hoteles_blueprint.route("/api/v1/hoteles/habitacion/<int:hab_id>", methods=["GET"])
def get_hotel_by_habid(hab_id):
    try:
        result = hotel_by_habid(hab_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún hotel que tenga esa habitación"}), 404

    result = result[0]
    return (
        result,
        200,
    )