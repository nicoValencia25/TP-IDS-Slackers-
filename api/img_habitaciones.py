from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

img_habitaciones_blueprint = Blueprint('img_habitaciones_blueprint', __name__)

QUERY_IMG_HABITACIONES = """
SELECT ImgHabitacionID, ImgHabitacion, TipoID
FROM ImgHabitaciones
"""

QUERY_IMG_HABITACION_BY_ID = """
SELECT ImgHabitacionID, ImgHabitacion, TipoID
FROM ImgHabitaciones
WHERE ImgHabitacionID = :ImgHabitacionID
"""

QUERY_IMG_HABITACION_ADD = """
INSERT INTO ImgHabitaciones (ImgHabitacionID, ImgHabitacion, TipoID)
VALUES (:ImgHabitacionID, :ImgHabitacion, :TipoID)
"""

QUERY_IMG_HABITACION_DELETE = """
DELETE FROM ImgHabitaciones WHERE ImgHabitacionID = :ImgHabitacionID
"""
    
def img_habitaciones_all():
    return run_query(QUERY_IMG_HABITACIONES)

def img_habitacion_by_id(img_hab_id):
    return run_query(QUERY_IMG_HABITACION_BY_ID, {"ImgHabitacionID": img_hab_id})

def img_habitacion_add(data):
    run_query(QUERY_IMG_HABITACION_ADD, data)

def img_habitacion_delete(img_hab_id):
    run_query(QUERY_IMG_HABITACION_DELETE, {'ImgHabitacionID': img_hab_id})
    
@img_habitaciones_blueprint.route("/api/v1/img_habitaciones", methods=["GET"])
def get_img_habitaciones():
    try:
        result = img_habitaciones_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200


@img_habitaciones_blueprint.route("/api/v1/img_habitaciones/<int:img_hab_id>", methods=["GET"])
def get_img_habitacion_by_id(img_hab_id):
    try:
        result = img_habitacion_by_id(img_hab_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún img_habitacion"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@img_habitaciones_blueprint.route("/api/v1/img_habitaciones", methods=["POST"])
def add_img_habitacion():
    data = request.get_json()

    keys = (
        "ImgHabitacionID",
        "ImgHabitacion",
        "TipoID"
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = img_habitacion_by_id(data["ImgHabitacionID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un img_habitacion con ese mismo ID"}), 400

        img_habitacion_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@img_habitaciones_blueprint.route('/api/v1/img_habitaciones/<int:img_hab_id>', methods=['DELETE'])
def delete_img_habitacion(img_hab_id):
    try:
        result = img_habitacion_by_id(img_hab_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el img_habitacion'}), 404

        img_habitacion_delete(img_hab_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        result,
        200,
    )