import hashlib
import mysql.connector
import config


class DB:
    def __init__(self):
        self.__connection = mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME
        )
        self.__cursor = self.__connection.cursor()

    def has_connection(self) -> bool:
        return self.__connection.is_connected()

    def __is_user(self, username: str) -> bool:
        self.__cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        users = self.__cursor.fetchall()

        if users:
            return True
        else:
            return False

    def create_user(self, name: str, username: str, email: str, password: str) -> bool:
        if self.__is_user(username):
            return False
        else:
            hashed_pass = hashlib.sha256(password.encode()).hexdigest()

            self.__cursor.execute("""INSERT INTO users (name, username, email, password)
                VALUES (%s, %s, %s, %s)
            """, (name, username, email, hashed_pass))

            self.__commit()

            return True

    def check_user(self, username: str, password: str) -> int | bool:
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        self.__cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_pass))
        users = self.__cursor.fetchall()

        if users:
            return users[0]
        else:
            return False

    def get_rooms(self) -> list[tuple]:
        self.__cursor.execute("SELECT * FROM rooms LIMIT 6")

        rooms = self.__cursor.fetchall()
        return rooms

    def get_room(self, room_id) -> tuple:
        self.__cursor.execute("SELECT * FROM rooms WHERE id = %s", (room_id,))

        room = self.__cursor.fetchone()
        return room

    def __commit(self) -> None:
        self.__connection.commit()

    def __close(self) -> None:
        self.__cursor.close()
        self.__connection.close()

            

