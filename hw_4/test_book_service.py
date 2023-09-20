import unittest
from unittest.mock import Mock

from book_service import BookService


class TestDataProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.book_srv = BookService(Mock())

    def test_notification_call(self):
        self.book_srv.book_info()
        self.book_srv.book_rep_obj.book_descrip.assert_called_with()
