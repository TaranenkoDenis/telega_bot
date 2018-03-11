import requests


class BotHandler:

    request_search_url = 'https://google.com/search?q='

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(
            self.api_url + method, data=params
        )
        return response.json()['result']

    def send_message(self, chat_id, text):
        text = text.replace(' ', '+')
        params = {'chat_id': chat_id, 'text': self.request_search_url + text}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, params)
        return response

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
