from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

servicios_blueprint = Blueprint('servicios_blueprint', __name__)

QUERY_SERVICIOS = """
SELECT ServicioID, Nombre, Precio, ImgServicio, HotelID, Descripcion, TipoDePago
FROM Servicios
"""

QUERY_SERVICIO_BY_ID = """
SELECT ServicioID, Nombre, Precio, ImgServicio, HotelID, Descripcion, TipoDePago
FROM Servicios
WHERE ServicioID = :ServicioID
"""

QUERY_SERVICIO_ADD = """
INSERT INTO servicios (ServicioID, Nombre, Precio, ImgServicio, HotelID, Descripcion, TipoDePago)
VALUES (:ServicioID, :Nombre, :Precio, :ImgServicio, :HotelID, :Descripcion, :TipoDePago)
"""

QUERY_SERVICIO_DELETE = """
DELETE FROM Servicios WHERE ServicioID = :ServicioID
"""
    
def servicios_all():
    return run_query(QUERY_SERVICIOS)

def servicio_by_id(hab_id):
    return run_query(QUERY_SERVICIO_BY_ID, {"ServicioID": hab_id})

def servicio_add(data):
    run_query(QUERY_SERVICIO_ADD, data)

def servicio_delete(hab_id):
    run_query(QUERY_SERVICIO_DELETE, {'ServicioID': hab_id})
    
@servicios_blueprint.route("/api/v1/servicios", methods=["GET"])
def get_servicios():
    try:
        result = servicios_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200


@servicios_blueprint.route("/api/v1/servicios/<int:hab_id>", methods=["GET"])
def get_servicio_by_id(hab_id):
    try:
        result = servicio_by_id(hab_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún servicio"}), 404

    result = result[0]
    return (jsonify(result), 200)


@servicios_blueprint.route("/api/v1/servicios", methods=["POST"])
def add_servicio():
    data = request.get_json()

    keys = (
        "ServicioID",
        "Nombre",
        "Precio",
        "ImgServicio",
        "HotelID",
        "Descripcion",
        "TipoDePago"
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = servicio_by_id(data["ServicioID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un servicio con ese mismo ID"}), 400

        servicio_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@servicios_blueprint.route('/api/v1/servicios/<int:hab_id>', methods=['DELETE'])
def delete_servicio(hab_id):
    try:
        result = servicio_by_id(hab_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el servicio'}), 404

        servicio_delete(hab_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (result, 200)