import telebot
from local_settings import local_settings
from messages_file import messages

bot = telebot.TeleBot(local_settings.BOT_TOKEN, parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    print('welcome is working')
    bot.send_message(chat_id=message.from_user.id,
                     text=messages.WELCOME)


# @bot.message_handler(commands=['search'])
# def search_handler(message):




if __name__ == "__main__":
    bot.infinity_polling()
