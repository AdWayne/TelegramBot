import telebot
from telebot import types

TOKEN = "7626771054:AAHm59eB7KLXvkAa13gZ7Ch73V88ysVWnDc"
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 Студенты")
    btn2 = types.KeyboardButton("📄 Тех док проект")
    btn3 = types.KeyboardButton("📊 Презентация")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработчик кнопки "Студенты"
@bot.message_handler(func=lambda message: message.text == "📚 Студенты")
def students_info(message):
    bot.send_message(message.chat.id, "👨‍🎓 количество работа студентов:\n1. Нығмет Азамат\n2. Задай Назым")

# Обработчик кнопки "Тех док проект" (отправка документа)
@bot.message_handler(func=lambda message: message.text == "📄 Тех док проект")
def send_tech_doc(message):
    with open("tech_doc.docx", "rb") as doc:
        bot.send_document(message.chat.id, doc)

# Обработчик кнопки "Презентация" (добавишь сам)
@bot.message_handler(func=lambda message: message.text == "📊 Презентация")
def send_presentation(message):
    bot.send_message(message.chat.id, "Здесь будет презентация работа Назыма 📂")

bot.polling()
