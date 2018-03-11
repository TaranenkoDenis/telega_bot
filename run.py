
from random import choice

from bot_handler import BotHandler

token = "558683310:AAFj6qJomJYESkp6WbzRxAWFfV8yQ-lp7IU"
greetings = ("Привет!", "Здравствуйте!", "Доброго времени суток!")


def main():
    new_offset = None

    my_bot = BotHandler(token)

    answered_update_id = 0

    while True:
        my_bot.get_updates(new_offset)

        last_update = my_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if answered_update_id != last_update_id:

            print("I have new message:\n")
            print("last_update_id = " + str(last_update_id))
            print("last_chat_text = " + str(last_chat_text))
            print("last_chat_id = " + str(last_chat_id))
            print("last_chat_name = " + str(last_chat_name))

            my_bot.send_message(last_chat_id, choice(greetings))
            answered_update_id = last_update_id


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
