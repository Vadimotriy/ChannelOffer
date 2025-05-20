import sqlite3


class MyDict:
    def __init__(self):
        self.connection = sqlite3.connect('data/data.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Messages (
        USER_ID INTEGER PRIMARY KEY,
        Text TEXT NOT NULL,
        Image TEXT NOT NULL,
        Processed INTEGER NOT NULL)''')

    def add_message(self, id, text, image='-', processed=0):
        self.cursor.execute('INSERT INTO Messages (USER_ID, Text, Image, Processed) VALUES (?, ?, ?, ?)',
                            (id, text, image, processed))
        self.connection.commit()

    def change_process(self, id, num):
        update = f"""UPDATE Messages SET Processed = ? WHERE USER_ID = ?"""
        self.cursor.execute(update, (num, id))
        self.connection.commit()
