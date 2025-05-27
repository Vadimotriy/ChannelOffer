import sqlite3


# класс для управления БД
class MyDict:
    # инициализация БД
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

    # добавление сообщения
    def add_message(self, id, num, text, name, image='-', processed=0):
        self.cursor.execute('INSERT INTO Messages (USER_ID, Num, Text, Image, Processed, Name_USER) VALUES (?, ?, ?, ?, ?, ?)',
                            (id, num, text, image, processed, name))
        self.connection.commit()

    # изменение состояние сообщения
    def change_process(self, id, num=1):
        update = f"UPDATE Messages SET Processed = ? WHERE Num = ?"
        self.cursor.execute(update, (num, id))
        self.connection.commit()

    # доставание последнего сообщения
    def get_data(self, num='*'):
        res = self.cursor.execute(f"SELECT {num} FROM Messages ORDER BY Num DESC LIMIT 1;").fetchone()
        self.connection.commit()

        res = res[0] if num == 'Num' else res
        return res

    # доставание сообщения по его номеру
    def get_data_from_num(self, num='*'):
        res = self.cursor.execute(f"SELECT * FROM Messages WHERE Num = {num}").fetchone()
        self.connection.commit()

        return res


# добавление строки для первого запуска/создания новой БД
if __name__ == '__main__':
    Users = MyDict()
    Users.add_message(1, 0, 'das', 'asd')