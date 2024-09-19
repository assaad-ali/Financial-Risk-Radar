from sqlalchemy import create_engine

def create_engine_connection(username: str, password: str, host: str, port: str, database: str):
    try:
        engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
        print("Connection to database successful.")
        return engine
    except Exception as e:
        print(f"Error: Could not connect to the database. {e}")
        return None

def close_connection(engine):
    try:
        engine.dispose()
        print("Connection closed.")
    except Exception as e:
        print(f"Error: Could not close the connection. {e}")
