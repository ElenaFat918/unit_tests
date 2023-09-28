from random import randint


class Contact:
    def __init__(self, name, number, address=None):
        self.__name = name
        self.__number = number
        self.__address = address

    def __str__(self):
        return f'{self.__name} - {self.__number}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address


class NoteBook:
    def __init__(self):
        self.__db = {}

    def add_contact(self, cnt: Contact):
        if len(self.__db) < 3:
            while True:
                uid = randint(0, 3)
                if not uid in self.__db:
                    self.__db[uid] = cnt
                    return f'Контакт успешно добавлен'
        else:
            return f'Записная книжка переполнена, удалите ненужные контакты'

    def edit_contact(self, uid, new_name=None, new_number=None, new_address=None):
        if uid in self.__db:
            if new_name is not None:
                self.__db[uid].name = new_name
            if new_number is not None:
                self.__db[uid].number = new_number
            if new_address is not None:
                self.__db[uid].address = new_address
            return f'Контакт успешно обновлён'
        else:
            return f'Контакт с таким ID не существует'

    def delete_contact(self, uid):
        if uid in self.__db:
            self.__db.pop(uid)
            return f'Контакт успешно удалён'
        else:
            return f'Контакт с таким ID не существует'

    def print_contacts(self):
        list_str = ''
        for key, value in self.__db.items():
            list_str += str(key) + ': ' + str(value) + '\n'
        return list_str

    def find_contact(self, uid=None, name=None, number=None):
        if uid is not None:
            if 0 <= uid <= 3:
                return f'{uid}: {self.__db[uid]}'
            else:
                return f'такого ID контакта не существует'
        elif name is not None:
            result = ''
            for key, value in self.__db.items():
                if value.name == name:
                    result += str(key) + ': ' + str(value) + '\n'
            if len(result) > 1:
                return result
            else:
                return f'Контакты с таким именем не найдены'
        elif number is not None:
            result = ''
            for key, value in self.__db.items():
                if value.number == number:
                    result += str(key) + ': ' + str(value) + '\n'
            if len(result) > 1:
                return result
            else:
                return f'Контакты с таким номером не найдены'
        else:
            return f'вы ввели некорректные параметры для поиска контакта'


if __name__ == '__main__':
    nb = NoteBook()
    con1 = Contact('Вася', '88888')
    con2 = Contact('Сава', '532385')
    con3 = Contact('Вася', '00000')
    nb.add_contact(con1)
    nb.add_contact(con2)
    nb.add_contact(con3)
    print(nb.print_contacts())
    print(nb.find_contact(name='Вася'))
    print(nb.find_contact(number='00000'))
    print(nb.find_contact(int(input('Введите ID контакта'))))
    print(nb.delete_contact(int(input('Введите ID контакта'))))
    print(nb.print_contacts())
    print(nb.edit_contact(int(input('Введите ID контакта')),
                          new_name=input('Введите имя контакта'),
                          new_number=input('Введите номер контакта')))
    print(nb.print_contacts())
