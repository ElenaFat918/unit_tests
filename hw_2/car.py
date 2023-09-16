from vehicle import Vehicle as Vhc


class Car(Vhc):
    STOP = 0
    MAX_SPEED = 60

    def __init__(self, company, model, year_release, wheels):
        self.__speed = self.STOP
        super().__init__(company, model, year_release, wheels)

    @property
    def speed_vehicle(self):
        return f'Скорость ТС = {self.__speed} км/ч' \


    @property
    def get_speed(self):
        return self.__speed

    def test_drive(self):
        self.__speed = self.MAX_SPEED

    def park(self):
        self.__speed = self.STOP


if __name__ == '__main__':
    car = Car('Panar Levasso', 'Type A', 1896, 4)
    print(car)
    print(car.speed_vehicle)
    car.test_drive()
    print(car.speed_vehicle)
    car.park()
    print(car.speed_vehicle)
