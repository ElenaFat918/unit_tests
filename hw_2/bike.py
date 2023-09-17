from vehicle import Vehicle as Vhc


class Bike(Vhc):
    STOP = 0
    MAX_SPEED = 75

    def __init__(self, company, model, year_release, wheels):
        self.__speed = self.STOP
        super().__init__(company, model, year_release, wheels)

    @property
    def speed_vehicle(self):
        return f'Скорость ТС = {self.__speed} км/ч'

    @property
    def get_speed(self):
        return self.__speed


    def test_drive(self):
        self.__speed = self.MAX_SPEED

    def park(self):
        self.__speed = self.STOP


if __name__ == '__main__':
    bike = Bike('Honda', 'Model A', 1948, 2)
    print(bike)
    print(bike.speed_vehicle)
    bike.test_drive()
    print(bike.speed_vehicle)
    bike.park()
    print(bike.speed_vehicle)

