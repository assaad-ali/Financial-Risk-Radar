from sqlalchemy import create_engine

# Replace with your credentials
username = 'root'
password = 'fsd2' 
host = 'localhost'
port = '3306'
staging_area = 'staging_db'

# Connection string construction
if password:
    connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{staging_area}'
else:
    connection_string = f'mysql+pymysql://{username}@{host}:{port}/{staging_area}'

# Create SQLAlchemy engine and test the connection
engine = create_engine(connection_string)

try:
    with engine.connect() as connection:
        print("Connection to the MySQL database was successful!")
except Exception as e:
    print(f"Failed to connect: {e}")
finally:
    engine.dispose()