import requests
from requests import request
import json


class WikiSearch:
    url = 'https://en.wikipedia.org/w/api.php'

    def __init__(self, text):
        self.input_text = text

    def get_result(self):
        response = requests.get(
            self.url,
            {
                'action': 'opensearch',
                'search': self.input_text,
                'limit': 1,
                'namespace': 0,
                'format': 'json'
            }

        )

        if response.status_code == 200:
            link = response.json()[3][0]
            if link:
                return link

