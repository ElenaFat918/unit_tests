import unittest
from unittest.mock import Mock

from http_service import WebService


class TestDataProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.data_web = WebService(Mock())

    def test_notification_call(self):
        self.data_web.request('https://gb.ru/education')
        self.data_web.client_obj.get.assert_called_once()
