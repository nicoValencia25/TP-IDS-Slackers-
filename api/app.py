from flask import Flask, jsonify
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
            jsonify(
                {
                    "UsuarioID": row[0],
                    "HabitacionID": row[1],
                    "ReservaCreacion": row[2],
                    "Desde": row[3],
                    "Hasta": row[4],
                    "CantAdultos": row[5],
                    "CantNiños": row[6],
                    "PrecioTotal": row[7],
                }
            )
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
                "UsuarioID": result[0],
                "HabitacionID": result[1],
                "ReservaCreacion": result[2],
                "Desde": result[3],
                "Hasta": result[4],
                "CantAdultos": result[5],
                "CantNiños": result[6],
                "PrecioTotal": result[7],
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(port="5001", debug=True)
