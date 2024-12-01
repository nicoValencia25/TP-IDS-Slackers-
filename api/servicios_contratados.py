from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

servicios_contratados_blueprint = Blueprint('servicios_contratados_blueprint', __name__)

QUERY_SERVICIOS_CONTRATADOS = """
SELECT ServicioContratadoID, Creacion, PrecioTotal, ServicioID, ReservaID
FROM ServicioContratado
"""

QUERY_SERVICIO_CONTRATADO_BY_ID = """
SELECT ServicioContratadoID, Creacion, PrecioTotal, ServicioID, ReservaID
FROM ServicioContratado 
WHERE ServicioContratadoID = :ServicioContratadoID
"""

QUERY_SERVICIO_CONTRATADO_ADD = """
INSERT INTO ServicioContratado (ServicioContratadoID, Creacion, PrecioTotal, ServicioID, ReservaID)
VALUES (:ServicioContratadoID, :Creacion, :PrecioTotal, :ServicioID, :ReservaID)
"""

QUERY_SERVICIO_CONTRATADO_DELETE = """
DELETE FROM ServicioContratado WHERE ServicioContratadoID = :ServicioContratadoID
"""

QUERY_SERVICIOS_CONTRATADOS_BY_RESERVAID = """
SELECT ServicioContratadoID, Creacion, PrecioTotal, ServicioID, ReservaID
FROM ServicioContratado 
WHERE ReservaID = :ReservaID
"""

def servicios_contratados_all():
    return run_query(QUERY_SERVICIOS_CONTRATADOS)

def servicio_contratado_by_id(serv_cont_id):
    return run_query(QUERY_SERVICIO_CONTRATADO_BY_ID, {"ServicioContratadoID": serv_cont_id})

def servicio_contratado_add(data):
    run_query(QUERY_SERVICIO_CONTRATADO_ADD, data)

def servicio_contratado_delete(serv_cont_id):
    run_query(QUERY_SERVICIO_CONTRATADO_DELETE, {'ServicioContratadoID': serv_cont_id})

def servicios_contratados_by_reservaid(res_id):
    return run_query(QUERY_SERVICIOS_CONTRATADOS_BY_RESERVAID, {"ReservaID": res_id})

@servicios_contratados_blueprint.route("/api/v1/servicios_contratados", methods=["GET"])
def get_servicios_contratados():
    try:
        result = servicios_contratados_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return(jsonify(result), 200)


@servicios_contratados_blueprint.route("/api/v1/servicios_contratados/<int:serv_cont_id>", methods=["GET"])
def get_servicio_contratado_by_id(serv_cont_id):
    try:
        result = servicio_contratado_by_id(serv_cont_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún servicio contratado"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@servicios_contratados_blueprint.route("/api/v1/servicios_contratados", methods=["POST"])
def add_servicio_contratado():
    data = request.get_json()

    keys = (
        "ServicioContratadoID",
        "Creacion",
        "PrecioTotal",
        "ServicioID",
        "ReservaID",
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = servicio_contratado_by_id(data["ServicioContratadoID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un servicio contratado con ese mismo ID"}), 400

        servicio_contratado_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@servicios_contratados_blueprint.route('/api/v1/servicios_contratados/<int:serv_cont_id>', methods=['DELETE'])
def delete_servicio_contratado(serv_cont_id):
    try:
        result = servicio_contratado_by_id(serv_cont_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el servicio contratado'}), 404

        servicio_contratado_delete(serv_cont_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        result,
        200,
    )

@servicios_contratados_blueprint.route("/api/v1/servicios_contratados/reserva/<int:res_id>", methods=["GET"])
def get_servicios_contratados_by_reservaid(res_id):
    try:
        result = servicios_contratados_by_reservaid(res_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún servicio contratado para esa reserva"}), 404

    return(jsonify(result), 200)