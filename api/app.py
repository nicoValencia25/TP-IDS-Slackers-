from flask import Flask, jsonify

import reservas

app = Flask(__name__)


@app.route("/api/v1/reservas/<int:res_id>", methods=["GET"])
def get_reservas_by_id(res_id):
    try:
        result = reservas.reservas_by_id(res_id)
    except Exception as e:
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
