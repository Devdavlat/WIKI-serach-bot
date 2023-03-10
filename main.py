import telebot
from environs import Env
from telebot.types import BotCommand
from wiki_file import wiki_config
from messages_file import messages

env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    print('welcome is working')
    bot.send_message(message.from_user.id, messages.WELCOME)


@bot.message_handler(commands=['search'])
def search_handler(message):
    print('search is working')
    msg = bot.send_message(chat_id=message.from_user.id, text=messages.SEARCH)
    bot.register_next_step_handler(msg, sear_wiki)


def sear_wiki(message):
    print('serach wiki is working')
    result_text = wiki_config.WikiSearch(message.text).get_result()
    if result_text is not None:
        bot.send_message(message.from_user.id, text=f"{result_text}")
    else:
        bot.send_message(message.from_user.id, text=messages.NOT_FOUND)


def my_commands():
    return [
        BotCommand('/start', 'Botni ishga tushurish'),
        BotCommand('/search', 'Malumotlarni qidirsh')
    ]


if __name__ == "__main__":
    print('started ...')
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
