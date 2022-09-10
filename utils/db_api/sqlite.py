

import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_messages(self):
        sql = """
        CREATE TABLE Messages (
            message_id varchar(50) NOT NULL,
            message_text varchar(2000) NOT NULL,
            name varchar(255) NOT NULL,
            user_id varchar(20) NOT NULL,
            tg_username varchar(50),
            PRIMARY KEY (message_id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_message(self, message_id: str, message_text: str , name: str, user_id: str, tg_username: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Messages(message_id, message_text, name, user_id, tg_username) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(message_id, message_text, name, user_id, tg_username), commit=True)

    def select_all_messages(self):
        sql = """
        SELECT * FROM Messages
        """
        return self.execute(sql, fetchall=True)

    def select_message(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Messages WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Messages;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Messages WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")