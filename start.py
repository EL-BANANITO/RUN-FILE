import gspread as gs
import telebot
from telebot import types

bot = telebot.TeleBot('Token')

json = gs.service_account(filename='json file name')
opensheet = json.open("google sheet file name").sheet1

row = opensheet.row_values("1")
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@bot.message_handler(commands=['start'])
def start(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Pc names")

    markup.add(item1)

    bot.send_message(message.chat.id, "lets start", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/help - explain all commands"
                                      "/start - start bot us only one time or if you update something"
                                      "r 'hostname' - run file on this Pc"
                                      "e 'hostname' - stop file on this pc"
                                      "for more information visit my github ")

@bot.message_handler(content_types=['text'])
def text(message):

    if message.chat.type == 'private':

        if message.text == 'Pc hostnames':
            bot.send_message(message.chat.id, str(row)[1:-1])

        elif (message.text[2:len(message.text)] in row) and message.text[0] == 'r':
            x = list[row.index(message.text[2:len(message.text)])]
            opensheet.update(x + "3", "yes")
        elif (message.text[2:len(message.text)] in row) and message.text[0] == 'e':
            x = list[row.index(message.text[2:len(message.text)])]
            opensheet.update(x + "3", "no")
        else:
            bot.send_message(message.chat.id, "I don't know this command, please write /help to see all the commands and what they do.")

bot.polling(none_stop=True)