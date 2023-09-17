from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, company, model, year_release, wheels,):
        self.__company = company
        self.__model = model
        self.__year_release = year_release
        self.__wheels = wheels

    @property
    def count_wheels(self):
        return self.__wheels

    def __str__(self):
        return f'ТС {self.__company}, ' \
               f'{self.__model}, ' \
               f'{self.__year_release}' \
               f'\n{self.__wheels} колеса'


    # def speed_vehicle(self):
    #     return f'Скорость ТС = {self.__speed}'

    @abstractmethod
    def test_drive(self):
        return 'Cкорость ТС'

    @abstractmethod
    def park(self):
        return 'Остановка ТС'


