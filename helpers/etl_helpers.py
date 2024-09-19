

import pandas as pd
from sqlalchemy import create_engine

def create_engine_connection(username: str, password: str, host: str, port: str, database: str):
    """
    Creates and returns an SQLAlchemy engine connection to the MySQL database.
    
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        host (str): MySQL host address.
        port (str): MySQL port number.
        database (str): Database name.
    
    Returns:
        engine (SQLAlchemy engine): SQLAlchemy engine object for database connection.
    """
    try:
        engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
        print("Connection to database successful.")
        return engine
    except Exception as e:
        print(f"Error: Could not connect to the database. {e}")
        return None

def load_dataframe_to_sql(engine, dataframe: pd.DataFrame, table_name: str, if_exists: str = 'append', chunksize: int = None):
    """
    Loads a pandas DataFrame into a SQL table.
    
    Args:
        engine: SQLAlchemy engine object.
        dataframe (pd.DataFrame): The pandas DataFrame to load.
        table_name (str): Name of the target SQL table.
        if_exists (str): What to do if the table already exists ('fail', 'replace', 'append').
        chunksize (int): The number of rows to write at a time. If None, writes all rows at once.
    """
    try:
        dataframe.to_sql(table_name, con=engine, if_exists=if_exists, index=False, chunksize=chunksize)
        print(f"Data successfully loaded into {table_name}.")
    except Exception as e:
        print(f"Error: Could not load data into {table_name}. {e}")

def close_connection(engine):
    """
    Closes the SQLAlchemy connection.
    
    Args:
        engine: SQLAlchemy engine object.
    """
    try:
        engine.dispose()
        print("Connection closed.")
    except Exception as e:
        print(f"Error: Could not close the connection. {e}")

# Example Usage

# Define your credentials and DataFrame
username = 'your_username'
password = 'your_password'
host = 'localhost'
port = '3306'
database = 'staging_db'

# Create the connection engine
engine = create_engine_connection(username, password, host, port, database)

# Assuming you have the 'us_companies' DataFrame
# us_companies = pd.read_csv('path_to_your_csv_file.csv')

if engine:
    # Load the DataFrame into the SQL table
    load_dataframe_to_sql(engine, us_companies, 'company_financials_staging', if_exists='append', chunksize=1000)
    
    # Close the connection
    close_connection(engine)
