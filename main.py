# _*_ coding: utf-8 _*_

import telebot
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    print('received help command')
    response = "Я Эскобар."
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['help'])
def handle_help(message):
    print('received help command')
    response = "— Почему группа называется именно «Бредор»?\n— А ну хер его знает, ну Бредор, мля, ну Бредор..."
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['ask'])
def handle_ask(message):
    print('received ask command')
    if "или" in message.text:
        response = "Шо то хуйня, шо это хуйня. Вот это обе хуйни такие, шо я, бля, ебал её маму у рот."
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'Шо?')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print('received a message')
    if "или" in message.text:
        response = "Шо то хуйня, шо это хуйня. Вот это обе хуйни такие, шо я, бля, ебал её маму у рот."
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'Шо?')


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        bot.answer_inline_query(inline_query.id, "йоу")
    except Exception as e:
        print(e)


bot.polling(none_stop=True, interval=0)
