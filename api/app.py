from flask import Flask, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

import reservas

app = Flask(__name__)


@app.route("/api/v1/reservas", methods=["GET"])
def get_reservas():
    try:
        result = reservas.reservas_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    response = []
    for row in result:
        response.append(
            {
                "ReservaID": row[0],
                "Creacion": row[1],
                "Desde": row[2],
                "Hasta": row[3],
                "CantNiños": row[4],
                "CantAdultos": row[5],
                "PrecioTotal": row[6],
                "HabID": row[7],
                "UsuarioID": row[8],
            }
        )

    return jsonify(response), 200


@app.route("/api/v1/reservas/<int:res_id>", methods=["GET"])
def get_reservas_by_id(res_id):
    try:
        result = reservas.reservas_by_id(res_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva"}), 404

    result = result[0]
    return (
        jsonify(
            {
                "ReservaID": result[0],
                "Creacion": result[1],
                "Desde": result[2],
                "Hasta": result[3],
                "CantNiños": result[4],
                "CantAdultos": result[5],
                "PrecioTotal": result[6],
                "HabID": result[7],
                "UsuarioID": result[8],
            }
        ),
        200,
    )


@app.route("/api/v1/reservas", methods=["POST"])
def post_reserva():
    data = request.get_json()

    keys = (
        "ReservaID",
        "Creacion",
        "Desde",
        "Hasta",
        "CantNiños",
        "CantAdultos",
        "PrecioTotal",
        "HabID",
        "UsuarioID",
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = reservas.reservas_by_id(data["ReservaID"])
        if len(result) > 0:
            return jsonify({"error": "Existe una reserva con ese mismo ID"}), 400

        reservas.reservas_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@app.route("/api/v1/reservas/<int:res_id>", methods=["DELETE"])
def delete_reservas(res_id):
    try:
        result = reservas.reservas_by_id(res_id)
        if len(result) == 0:
            return jsonify({"error": "No se encontró la reserva"}), 404

        reservas.reservas_remove(res_id)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    result = result[0]
    return (
        jsonify(
            {
                "ReservaID": res_id,
                "Creacion": result[1],
                "Desde": result[2],
                "Hasta": result[3],
                "CantNiños": result[4],
                "CantAdultos": result[5],
                "PrecioTotal": result[6],
                "HabID": result[7],
                "UsuarioID": result[8],
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(port="5001", debug=True)
