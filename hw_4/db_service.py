class Database:
    def __init__(self, lst: list):
        self.db_list = lst

    def query(self, sql: str):
        print(f'Получен запрос {sql} для {self.db_list}')


class DataProcessor:
    def __init__(self, db: Database):
        self.__db = db

    @property
    def db_obj(self):
        return self.__db

    def db_sql(self, sql: str):
        self.__db.query(sql)
