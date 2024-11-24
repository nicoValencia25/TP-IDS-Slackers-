from sqlalchemy import text
from config import engine

def run_query(query, parameters=None):
    
    with engine.connect() as connection:
        result = connection.execute(text(query), parameters)
        connection.close()

    return [dict(row) for row in result]