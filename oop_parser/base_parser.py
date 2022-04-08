import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

class BaseParser:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.headers = {}

    def set_proxy(self):
        pass
        # self.proxy = proxy

    def _set_user_agent(self):
        ua = UserAgent()
        self.headers['User-Agent'] = ua.random

    def get(self, url):
        self._set_user_agent()
        response = requests.get(url, headers = self.headers)
        return response.text

    def init_soup(self, html) -> None:
        soup = BS(html, 'lxml')
        return soup

    # полиморфные методы почему? Вызов один, но выполнение разное. Интерфейс один, но разное тело
    def get_links_data(self):
        raise NotImplementedError
    
    # полиморфные методы
    def get_details_data(self):
        raise NotImplementedError