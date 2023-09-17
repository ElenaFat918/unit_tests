import unittest
from user_repository import UserRepository as Usrep
from user import User

MESSAGE = 'Ожидаемые сообщения не совпадают'


class TestUsRep(unittest.TestCase):
    def setUp(self) -> None:
        self.us_rep = Usrep()
        self.user = User('login', 'password')

# ---------------------------------------------------------------------------------------
    def test_successful_authenticate(self):
        self.user.authenticate(self.user.login, self.user.password)
        self.assertTrue(self.user.is_authenticate)

    def test_failed_authenticate_wrong_login(self):
        self.user.authenticate('', self.user.password)
        self.assertFalse(self.user.is_authenticate)

    def test_failed_authenticate_wrong_password(self):
        self.user.authenticate(self.user.login, '')
        self.assertFalse(self.user.is_authenticate)

    def test_failed_authenticate_wrong_login_and_password(self):
        self.user.authenticate('', '')
        self.assertFalse(self.user.authenticate('', ''))

    # ---------------------------------------------------------------------------------------
    def test_add_user_deactivate_session(self):
        self.assertEqual(self.us_rep.add_user('1', '11'), "You aren't authentication", MESSAGE)

    def test_activate_session(self):
        self.assertEqual(self.us_rep.activate_session('bhbk', 'njknlkn'), "You can't activate the session!", MESSAGE)
        self.assertEqual(self.us_rep.activate_session('admin', 'kklnl'), "You can't activate the session!", MESSAGE)
        self.assertEqual(self.us_rep.activate_session('njknjk', 'adm'), "You can't activate the session!", MESSAGE)
        self.assertEqual(self.us_rep.activate_session('admin', 'adm'), 'The session is active', MESSAGE)
        self.assertEqual(self.us_rep.activate_session('admin', 'adm'), 'The session is already active', MESSAGE)

    def test_add_user_activate_session(self):
        self.us_rep.activate_session('admin', 'adm')
        self.assertEqual(self.us_rep.add_user('Maxim', 'Max89'), 'New User is created', MESSAGE)

    def test_deactivate_session(self):
        self.us_rep.activate_session('admin', 'adm')
        self.assertEqual(self.us_rep.deactivate_session(), 'The session is over', MESSAGE)

    def test_activate_session_by_new_user(self):
        self.us_rep.activate_session('admin', 'adm')
        self.us_rep.add_user('Maxim', 'Max89')
        self.us_rep.deactivate_session()
        self.assertEqual(self.us_rep.activate_session('Maxim', 'Max89'), "The session is active", MESSAGE)

