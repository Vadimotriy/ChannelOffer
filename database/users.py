import sqlite3


class MyDict:
    def __init__(self):
        self.connection = sqlite3.connect('data/data.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Messages (
        USER_ID INTEGER NOT NULL,
        Num INTEGER NOT NULL,
        Text TEXT NOT NULL,
        Image TEXT NOT NULL,
        Processed INTEGER NOT NULL,
        Name_USER TEXT NOT NULL)''')

    def add_message(self, id, num, text, name, image='-', processed=0):
        self.cursor.execute('INSERT INTO Messages (USER_ID, Num, Text, Image, Processed, Name_USER) VALUES (?, ?, ?, ?, ?, ?)',
                            (id, num, text, image, processed, name))
        self.connection.commit()

    def change_process(self, id, num=1):
        update = f"UPDATE Messages SET Processed = ? WHERE Num = ?"
        self.cursor.execute(update, (num, id))
        self.connection.commit()

    def get_data(self, num='*'):
        res = self.cursor.execute(f"SELECT {num} FROM Messages ORDER BY Num DESC LIMIT 1;").fetchone()
        self.connection.commit()

        res = res[0] if num == 'Num' else res
        return res

    def get_data_from_num(self, num='*'):
        res = self.cursor.execute(f"SELECT * FROM Messages WHERE Num = {num}").fetchone()
        self.connection.commit()

        return res
