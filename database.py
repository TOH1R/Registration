import sqlite3



class DataBase():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()


    def create_table_users(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT,
            )""")
        self.db.commit()
        
        
    def add_user(self, user_id, user_full_name):
        self.cursor.execute("""
                    INSERT INTO users (id, full_name) VALUES (?, ?)
                    """, (user_id, user_full_name))
        self.dp.commit()

    def select_user(self):
        user_select = self.cursor.exucute("""
        select * from users
        """)
        return user_select.fetchall()



    def close_database(self):
        self.db.close()



