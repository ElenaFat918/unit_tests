import unittest
from unittest.mock import Mock

from message_service import NotificationService


class TestNotificate(unittest.TestCase):
    def setUp(self) -> None:
        self.not_serv = NotificationService(Mock())

    def test_notification_call(self):
        self.not_serv.notification()
        self.not_serv.msg_srv.send_message.assert_called_once()
