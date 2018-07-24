from random import choice

from bot.telegram_bot import TelegramBot


def main():
    bot = TelegramBot("558683310:AAFj6qJomJYESkp6WbzRxAWFfV8yQ-lp7IU")
    bot.start_working()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
