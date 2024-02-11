import mysql.connector
from mysql.connector import Error

def create_db():
    # Local variables that will be initialized as the connection and cursor
    connection = None
    cursor = None
    try:
        # Establishing a connection to the MySQL database
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Server address
            user="root",  # User name
            password="1111",  # Password
            database="testDB"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()

            # Reading the SQL script from a file
            with open("../queries/database_setup.sql", "r") as f:
                sql = f.read()
                # Splitting the script into individual queries
                sql_commands = sql.split(';')
                # Executing each SQL command
                for command in sql_commands:
                    try:
                        if command.strip() != '':
                            cursor.execute(command)
                    except Error as cmd_exec_error:
                        print(f"Error occurred: {cmd_exec_error}")

            # Committing any changes to the database
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Closing cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_db()
