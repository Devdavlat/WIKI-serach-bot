import telebot
from local_settings import local_settings

bot = telebot.TeleBot(local_settings.BOT_TOKEN, parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    print('welocme is working')
    bot.send_message(chat_id=message.from_user.id,
                     text='Salom')


if __name__ == "__main__":
    bot.infinity_polling()
