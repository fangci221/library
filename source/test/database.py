import os
import pymysql
from dotenv import load_dotenv


def connect_mysql():

    # Load environment variables from .env
    load_dotenv()

    # Set connection parameters
    config = {
        'user': os.getenv('DB_USER'),
        'passwd': os.getenv('DB_PASSWD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'db': os.getenv('DB_NAME')
    }
    
    # Connect to the database
    try:
        cnx = pymysql.connect(**config)
    except pymysql.err.OperationalError as e:
        print(f"Can't connect to MySQL database: {e}")
        return None
    else:
        return cnx


if __name__ == "__main__":
    cnx = connect_mysql()
    print("Connection is OK")
    cnx.close()
