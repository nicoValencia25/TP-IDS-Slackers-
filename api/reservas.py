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

engine = create_engine("mysql://root:root@localhost:3306/HotelDB")
# engine = create_engine("mysql+mysqlconnector://root@localhost:3306/HotelDB")


def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()

    return result


def reservas_all():
    return run_query(QUERY_RESERVAS).fetchall()


def reservas_by_id(res_id):
    return run_query(QUERY_RESERVAS_BY_ID, {"res_id": res_id}).fetchall()
