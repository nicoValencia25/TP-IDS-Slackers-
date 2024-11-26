from flask import jsonify, request, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from api.db_utils import run_query

usuarios_blueprint = Blueprint('usuarios_blueprint', __name__)

QUERY_USUARIOS = """
SELECT UsuarioID, Nombre, Apellido, Nacimiento, Email, Contraseña, Telefono, DNI, Pais
FROM Usuarios
"""

QUERY_USUARIO_BY_ID = """
SELECT UsuarioID, Nombre, Apellido, Nacimiento, Email, Contraseña, Telefono, DNI, Pais
FROM Usuarios
WHERE UsuarioID = :UsuarioID
"""

QUERY_USUARIO_ADD = """
INSERT INTO Usuarios (UsuarioID, Nombre, Apellido, Nacimiento, Email, Contraseña, Telefono, DNI, Pais)
VALUES (:UsuarioID, :Nombre, :Apellido, :Nacimiento, :Email, :Contraseña, :Telefono, :DNI, :Pais)
"""

QUERY_USUARIO_DELETE = """
DELETE FROM Usuarios WHERE UsuarioID = :UsuarioID
"""
    
def usuarios_all():
    return run_query(QUERY_USUARIOS)

def usuario_by_id(user_id):
    return run_query(QUERY_USUARIO_BY_ID, {"UsuarioID": user_id})

def usuario_add(data):
    run_query(QUERY_USUARIO_ADD, data)

def usuario_delete(user_id):
    run_query(QUERY_USUARIO_DELETE, {'UsuarioID': user_id})
    
@usuarios_blueprint.route("/api/v1/usuarios", methods=["GET"])
def get_usuarios():
    try:
        result = usuarios_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return(jsonify(result), 200)


@usuarios_blueprint.route("/api/v1/usuarios/<int:user_id>", methods=["GET"])
def get_usuario_by_id(user_id):
    try:
        result = usuario_by_id(user_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ningún usuario"}), 404

    result = result[0]
    return (
        result,
        200,
    )


@usuarios_blueprint.route("/api/v1/usuarios", methods=["POST"])
def add_usuario():
    data = request.get_json()

    keys = (
        "UsuarioID",
        "Nombre",
        "Apellido",
        "Nacimiento",
        "Email",
        "Contraseña",
        "Telefono",
        "DNI",
        "Pais"
    )

    for key in keys:
        if key not in data:
            return jsonify({"error": f"Faltan el dato {key}"}), 400

    try:
        result = usuario_by_id(data["UsuarioID"])
        if len(result) > 0:
            return jsonify({"error": "Existe un usuario con ese mismo ID"}), 400

        usuario_add(data)

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data), 201


@usuarios_blueprint.route('/api/v1/usuarios/<int:user_id>', methods=['DELETE'])
def delete_usuario(user_id):
    try:
        result = usuario_by_id(user_id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el usuario'}), 404

        usuario_delete(user_id)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return (
        result,
        200,
    )