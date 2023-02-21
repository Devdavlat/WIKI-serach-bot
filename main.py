import telebot
from telebot.types import BotCommand
from wiki_file import wiki_config
from local_settings import local_settings
from messages_file import messages

bot = telebot.TeleBot(local_settings.BOT_TOKEN, parse_mode='html')


@bot.message_handler(commands=['s'])
def welcome(message):
    print('welcome is working')
    bot.send_message(chat_id=message.from_user.id,
                     text=messages.WELCOME)


@bot.message_handler(commands=['search'])
def search_handler(message):
    msg = bot.send_message(chat_id=message.from_user.id, text=messages.SEARCH)
    bot.register_next_step_handler(msg, sear_wiki)


def sear_wiki(message):
    result_text = wiki_config.WikiSearch(message.text).get_result()
    print(result_text)


def my_commands():
    return [
        BotCommand('/s', 'Botni ishga tushurish'),
        BotCommand('/search', 'Malumotlarni qidirsh')
    ]


if __name__ == "__main__":
    print('started ...')
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
