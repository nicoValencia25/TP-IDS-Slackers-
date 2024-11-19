from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text

QUERY_RESERVAS = """
SELECT ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabID, UsuarioID
FROM Reservas
"""

QUERY_RESERVAS_BY_ID = """
SELECT ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabID, UsuarioID
FROM Reservas
WHERE ReservaID = :res_id
"""

QUERY_RESERVAS_ADD = """
INSERT INTO Reservas (ReservaID, Creacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabID, UsuarioID)
VALUES (:ReservaID, :Creacion, :Desde, :Hasta, :CantNiños, :CantAdultos, :PrecioTotal, :HabID, :UsuarioID)
"""

QUERY_RESERVAS_REMOVE = """
DELETE FROM Reservas WHERE ReservaID = :ReservaID
"""


engine = create_engine("mysql://root:root@localhost:3306/HotelBD")
# engine = create_engine("mysql+mysqlconnector://root@localhost:3306/HotelBD")


def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()

    return result


def reservas_all():
    return run_query(QUERY_RESERVAS).fetchall()


def reservas_by_id(res_id):
    return run_query(QUERY_RESERVAS_BY_ID, {"res_id": res_id}).fetchall()


def reservas_add(data):
    run_query(QUERY_RESERVAS_ADD, data)


def reservas_remove(res_id):
    run_query(QUERY_RESERVAS_REMOVE, {'ReservaID': res_id})
