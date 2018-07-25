import argparse

from bot.telegram_bot import TelegramBot


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'token',
        help='Token for access the HTTP API from BotFather',
        type=str
    )
    return parser.parse_args()


def main():
    args = get_arguments()
    bot = TelegramBot(args.token)
    bot.start_working()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
