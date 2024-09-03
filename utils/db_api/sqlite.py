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

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id varchar(255),
            kon7 varchar(255),
            kon18 varchar(255),
            kon36 varchar(255),
            kon65 varchar(255),
            kon95 varchar(255)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, user_id: str, kon7: str = None, kon18: str = None, kon36: str = None, kon65: str = None,
                 kon95: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, kon7, kon18, kon36, kon65, kon95) VALUES(?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, kon7, kon18, kon36, kon65, kon95), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_kon7(self, kon7, user_id):
        sql = f"""
        UPDATE Users SET kon7=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(kon7, user_id), commit=True)

    def update_user_kon18(self, kon18, user_id):
        sql = f"""
        UPDATE Users SET kon18=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(kon18, user_id), commit=True)

    def update_user_kon36(self, kon36, user_id):
        sql = f"""
        UPDATE Users SET kon36=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(kon36, user_id), commit=True)

    def update_user_kon65(self, kon65, user_id):
        sql = f"""
        UPDATE Users SET kon65=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(kon65, user_id), commit=True)

    def update_user_kon95(self, kon95, user_id):
        sql = f"""
        UPDATE Users SET kon95=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(kon95, user_id), commit=True)




    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
