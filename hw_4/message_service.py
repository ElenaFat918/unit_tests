class MessageService:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient

    def send_message(self):
        print(f'{self.message} для {self.recipient}')


class NotificationService:
    def __init__(self, _message_service: MessageService):
        self._message_service = _message_service

    @property
    def msg_srv(self):
        return self._message_service

    def notification(self):
        self._message_service.send_message()
