import unittest
from unittest.mock import Mock

from note_book import Contact, NoteBook

class TestNoteBook(unittest.TestCase):
    def setUp(self):
        self.cnt = Contact('Вася', '88888')
        self.nb = NoteBook()
        self.fake_cnt = Mock()

    def test_add_contact(self):
        self.assertEqual(self.nb.add_contact(self.fake_cnt), f'Контакт успешно добавлен')

