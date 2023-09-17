"""
Добавьте класс UserRepository для управления пользователями.
В этот класс должен быть включен метод add_user, который добавляет пользователя в систему,
если он прошел аутентификацию. Покройте тестами новую функциональность
"""
from user import User


class UserRepository:
    def __init__(self):
        self.__users = [User('admin', 'adm')]
        self.__session = False

    def add_user(self, new_login, new_password):
        if self.__session:
            self.__users.append(User(new_login, new_password))
            return 'New User is created'
        else:
            return "You aren't authentication"

    def activate_session(self, user_login, user_password):
        if not self.__session:
            for user in self.__users:
                user.authenticate(user_login, user_password)
                if user.is_authenticate:
                    self.__session = user.is_authenticate
                    return 'The session is active'
            else:
                return "You can't activate the session!"
        else:
            return 'The session is already active'

    def deactivate_session(self):
        self.__session = False
        return 'The session is over'


# if __name__ == '__main__':
#     u_r = UserRepository()
#     print(u_r.add_user('Ivan', 'Dm123'))
#     print(u_r.activate_session('Valentin', 'Val123'))
#     print(u_r.activate_session('admin', 'mda'))
#     print(u_r.activate_session('admin', 'adm'))
#     print(u_r.add_user('Mihail', 'Mih321'))
#     print(u_r.deactivate_session())
#     print(u_r.activate_session('Mihail', 'Mih321'))
