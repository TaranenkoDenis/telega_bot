import requests


class TelegaRequestsHelper:

    REQUEST_TELEGA_GET_UPDATES = 'getUpdates'
    REQUEST_TELEGA_SEND = 'getUpdates'

    def __init__(self, telega_api_url):
        self.telega_api_url = telega_api_url

    def get_updates(self, offset=None, timeout=30):
        url = self.telega_api_url + self.REQUEST_TELEGA_GET_UPDATES
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(url, data=params)
        return response.json()['result']

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        url = '{}{}'.format(self.telega_api_url,'sendMessage')
        response = requests.post(url, data=params)
        return response

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
