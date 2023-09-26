import unittest
from unittest.mock import Mock

from db_service import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.data_proc = DataProcessor(Mock())

    def test_notification_call(self):
        self.data_proc.db_sql('sql-post')
        self.data_proc.db_obj.query.assert_called_once()
