from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

QUERY_RESERVAS = """
SELECT ReservaID, ReservaCreacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabitacionID, UsuarioID
FROM Reservas
"""

QUERY_RESERVA_BY_ID = """
SELECT ReservaID, ReservaCreacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabitacionID, UsuarioID
FROM Reservas
WHERE ReservaID = :ReservaID
"""

QUERY_RESERVA_ADD = """
INSERT INTO Reservas (ReservaID, ReservaCreacion, Desde, Hasta, CantNiños, CantAdultos, PrecioTotal, HabitacionID, UsuarioID)
VALUES (:ReservaID, :ReservaCreacion, :Desde, :Hasta, :CantNiños, :CantAdultos, :PrecioTotal, :HabitacionID, :UsuarioID)
"""

QUERY_RESERVA_DELETE = """
DELETE FROM Reservas WHERE ReservaID = :ReservaID
"""

QUERY_HABITACIONES = """
SELECT HabitacionID, HotelID, NumHabitacion, Piso, TipoDeHabitacion, CantHuespedes, Descripcion, Superficie, PrecioAdulto, PrecioNiño
FROM Habitaciones
"""

QUERY_HABITACION_BY_ID = """
SELECT HabitacionID, HotelID, NumHabitacion, Piso, TipoDeHabitacion, CantHuespedes, Descripcion, Superficie, PrecioAdulto, PrecioNiño
FROM Habitaciones
WHERE HabitacionID = :HabitacionID
"""

QUERY_HABITACION_ADD = """
INSERT INTO Habitaciones (HabitacionID, HotelID, NumHabitacion, Piso, TipoDeHabitacion, CantHuespedes, Descripcion, Superficie, PrecioAdulto, PrecioNiño)
VALUES (:HabitacionID, :HotelID, :NumHabitacion, :Piso, :TipoDeHabitacion, :CantHuespedes, :Descripcion, :Superficie, :PrecioAdulto, :PrecioNiño)
"""

QUERY_HABITACION_DELETE = """
DELETE FROM Habitaciones WHERE HabitacionID = :HabitacionID
"""


def run_query(query, parameters=None):
    with db.engine.connect() as connection:
        result = connection.execute(text(query), parameters)

    return [dict(row) for row in result]


def reservas_all():
    return run_query(QUERY_RESERVAS)


def reserva_by_id(res_id):
    return run_query(QUERY_RESERVA_BY_ID, {"ReservaID": res_id})


def reserva_add(data):
    run_query(QUERY_RESERVA_ADD, data)


def reserva_delete(res_id):
    run_query(QUERY_RESERVA_DELETE, {'ReservaID': res_id})
    
def habitaciones_all():
    return run_query(QUERY_HABITACIONES)

def habitacion_by_id(hab_id):
    return run_query(QUERY_HABITACION_BY_ID, {"HabitacionID": hab_id})


def habitacion_add(data):
    run_query(QUERY_HABITACION_ADD, data)


def habitacion_delete(hab_id):
    run_query(QUERY_HABITACION_DELETE, {'HabitacionID': hab_id})