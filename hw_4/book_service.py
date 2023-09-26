"""
У вас есть класс BookService,
который использует абстрактный класс BookRepository
для получения информации о книгах из базы данных.
Ваша задача написать unit-тесты для BookService,
используя Mock для создания мок-объекта BookRepository.
"""


class BookRepository:
    def __init__(self, name, autor, description):
        self.__name = name
        self.__autor = autor
        self.__description = description

    def __str__(self):
        return f'{self.__name}, {self.__autor}'

    def book_descrip(self):
        print(f'{self.__name} : \n{self.__description}')


class BookService:
    def __init__(self, book_rep: BookRepository):
        self.__book_rep = book_rep

    @property
    def book_rep_obj(self):
        return self.__book_rep

    def book_info(self):
        self.__book_rep.book_descrip()
