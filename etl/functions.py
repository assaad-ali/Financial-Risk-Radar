from sqlalchemy import create_engine
import pandas as pd

def load_dataframe_to_sql(engine, dataframe: pd.DataFrame, table_name: str, if_exists: str = 'append', chunksize: int = None):
    try:
        dataframe.to_sql(table_name, con=engine, if_exists=if_exists, index=False, chunksize=chunksize)
        print(f"Data successfully loaded into {table_name}.")
    except Exception as e:
        print(f"Error: Could not load data into {table_name}. {e}")

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
