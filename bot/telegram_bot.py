from bot.requests_helper import TelegaRequestsHelper


class TelegramBot:
    REQUEST_SEARCH_URL = 'https://google.com/search?q='

    def __init__(self, token):
        self.requests_helper = TelegaRequestsHelper(
            "https://api.telegram.org/bot{}/".format(token)
        )

    def _get_redirect_message(self, request_text):
        text = request_text.replace(' ', '+')
        text = self.REQUEST_SEARCH_URL + text
        return text

    def start_working(self):
        answered_update_id = 0

        while True:
            last_update = self.requests_helper.get_last_update()

            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

            if answered_update_id != last_update_id:

                answered_update_id = last_update_id

                print("new message!")
                print("last_update_id = {0}".format(last_update_id))
                print("last_chat_text = {0}".format(last_chat_text))
                print("last_chat_id = {0}".format(last_chat_id))
                print("last_chat_name = {0}".format(last_chat_name))

                self.requests_helper.send_message(
                    last_chat_id, 
                    self._get_redirect_message(last_chat_text) 
                )
