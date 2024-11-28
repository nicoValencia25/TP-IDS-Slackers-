from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

reservas_blueprint = Blueprint('reservas_blueprint', __name__)

QUERY_RESERVAS = """
SELECT ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabitacionID, UsuarioID
FROM Reservas
"""

QUERY_RESERVA_BY_ID = """
SELECT ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabitacionID, UsuarioID
FROM Reservas
WHERE ReservaID = :ReservaID
"""

QUERY_RESERVA_ADD = """
INSERT INTO Reservas (ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabitacionID, UsuarioID)
VALUES (:ReservaID, :Creacion, :Desde, :Hasta, :CantNiños, :CantAdultos, :PrecioTotal, :HabitacionID, :UsuarioID)
"""

QUERY_RESERVA_DELETE = """
DELETE FROM Reservas WHERE ReservaID = :ReservaID
"""

QUERY_RESERVA_BY_APELLIDO = """
SELECT ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabID, Reservas.UsuarioID, Apellido 
FROM Reservas
INNER JOIN Usuarios on Usuarios.UsuarioID = Reservas.UsuarioID
WHERE Apellido = :Apellido and ReservaID = :ReservaID
"""

def reservas_all():
    return run_query(QUERY_RESERVAS)


def reserva_by_id(res_id):
    return run_query(QUERY_RESERVA_BY_ID, {"ReservaID": res_id})

def reserva_add(data):
    run_query(QUERY_RESERVA_ADD, data)

def reserva_delete(res_id):
    run_query(QUERY_RESERVA_DELETE, {'ReservaID': res_id})

def reserva_by_id_and_apellido(res_id, apellido):
    return run_query(QUERY_RESERVA_BY_APELLIDO, {'ReservaID': res_id, 'Apellido': apellido})

@reservas_blueprint.route("/api/v1/reservas", methods=["GET"])
def get_reservas():
    try:
        result = reservas_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return(jsonify(result), 200)


@reservas_blueprint.route("/api/v1/reservas/<int:res_id>", methods=["GET"])
def get_reserva_by_id(res_id):
    try:
        result = reserva_by_id(res_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@reservas_blueprint.route("/api/v1/reservas", methods=["POST"])
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


@reservas_blueprint.route('/api/v1/reservas/<int:res_id>', methods=['DELETE'])
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
        result,
        200,
    )

@reservas_blueprint.route("/api/v1/reservas/<int:res_id>/<str:apellido>", methods=["GET"])
def get_reserva_by_id_and_apellido(res_id, apellido):
    try:
        result = reserva_by_id_and_apellido(res_id, apellido)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva, para ese apellido"}), 404

    result = result[0]
    return (
        result,
        200,
    )