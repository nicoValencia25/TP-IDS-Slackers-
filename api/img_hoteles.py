from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

img_hoteles_blueprint = Blueprint('img_hoteles_blueprint', __name__)

QUERY_IMG_HOTELES = """
SELECT ImgHotelID, ImgHotel, HotelID
FROM ImgHoteles
"""

QUERY_IMG_HOTEL_BY_ID = """
SELECT ImgHotelID, ImgHotel, HotelID
FROM ImgHoteles
WHERE ImgHotelID = :ImgHotelID
"""

QUERY_IMG_HOTEL_ADD = """
INSERT INTO ImgHoteles (ImgHotelID, ImgHotel, HotelID)
VALUES (:ImgHotelID, :ImgHotel, :HotelID)
"""

QUERY_IMG_HOTEL_DELETE = """
DELETE FROM ImgHoteles WHERE ImgHotelID = :ImgHotelID
"""
    
def img_hoteles_all():
    return run_query(QUERY_IMG_HOTELES)

def img_hotel_by_id(img_hotel_id):
    return run_query(QUERY_IMG_HOTEL_BY_ID, {"ImgHotelID": img_hotel_id})

def img_hotel_add(data):
    run_query(QUERY_IMG_HOTEL_ADD, data)

def img_hotel_delete(img_hotel_id):
    run_query(QUERY_IMG_HOTEL_DELETE, {'ImgHotelID': img_hotel_id})
    
@img_hoteles_blueprint.route("/api/v1/img_hoteles", methods=["GET"])
def get_img_hoteles():
    try:
        result = img_hoteles_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200


@img_hoteles_blueprint.route("/api/v1/img_hoteles/<int:img_hotel_id>", methods=["GET"])
def get_img_hotel_by_id(img_hotel_id):
    try:
        result = img_hotel_by_id(img_hotel_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún img_hotel"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@img_hoteles_blueprint.route("/api/v1/img_hoteles", methods=["POST"])
def add_img_hotel():
    data = request.get_json()

    keys = (
        "ImgHotelID",
        "ImgHotel",
        "HotelID",
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = img_hotel_by_id(data["ImgHotelID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un img_hotel con ese mismo ID"}), 400

        img_hotel_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@img_hoteles_blueprint.route('/api/v1/img_hoteles/<int:img_hotel_id>', methods=['DELETE'])
def delete_img_hotel(img_hotel_id):
    try:
        result = img_hotel_by_id(img_hotel_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el img_hotel'}), 404

        img_hotel_delete(img_hotel_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        result,
        200,
    )