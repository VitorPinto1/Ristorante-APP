import mysql.connector
from mysql.connector import Error
from werkzeug.security import check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.environ.get('MYSQL_DATABASE_HOST')
db_user = os.environ.get('MYSQL_USER')
db_password = os.environ.get('MYSQL_PASSWORD')
db_name = os.environ.get('MYSQL_DATABASE')
db_port = os.environ.get('MYSQL_PORT')

class DatabaseService:
    def __init__(self):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.db_port = db_port
    
    def _get_connection(self):
        return mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name,
            port=self.db_port
        )

    def userName(self, name):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    query = "SELECT * FROM users WHERE name = %s"
                    cursor.execute(query, (name,))
                    user = cursor.fetchone()
            return user
        except Error as err:
            print(f"Error: {err}")
            return None

    def check_password(self, stored_password_hash, provided_password):
        return check_password_hash(stored_password_hash, provided_password)

    def userReservation(self, user_id):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    query = """
                        SELECT *
                        FROM reservation
                        WHERE user_id = %s
                    """
                    cursor.execute(query, (user_id,))
                    reservations = cursor.fetchall()
            return reservations
        except Error as err:
            print(f"Error: {err}")
            return []
    
    def update_reservation(self, reservation_id, date, time, total_guests):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    query = """
                        UPDATE reservation
                        SET day = %s, time = %s, totalPerson = %s
                        WHERE id = %s
                    """
                    cursor.execute(query, (date, time, total_guests, reservation_id))
                    conn.commit()
        except Error as err:
            print(f"Error: {err}")

