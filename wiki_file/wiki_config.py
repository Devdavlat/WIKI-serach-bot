import requests


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
        print(self.input_text)
        print(response.status_code)
        if response.status_code == 200:
            link = None
            try:
                link = response.json()[3][0]
            except IndexError as e:
                print(e)

            if link:
                return link
            else:
                return None
