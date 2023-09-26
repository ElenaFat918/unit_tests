class HttpClient:
    def __init__(self, ip: str):
        self.__ip = ip

    def get(self, url: str):
        print(f'Поступил HTTP-запрос {url} от  {self.__ip}')


class WebService:
    def __init__(self, http_cl: HttpClient):
        self.__http_cl = http_cl

    @property
    def client_obj(self):
        return self.__http_cl

    def request(self, url: str):
        self.__http_cl.get(url)
