import telebot
from telebot import types

TOKEN = '7752147800:AAGskc5yPs2me4VMU3U2PYMJwz6F3VLQ1DI'
bot = telebot.TeleBot(TOKEN)

# Список администраторов (по ID пользователей)
admin_ids = [1643330789, 987654321]  # Здесь указаны ID администраторов

# База данных пользователей (например, список имен или словарь)
user_data = {}

# Хендлер для команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    if user_id not in user_data:
        user_data[user_id] = {"name": message.chat.first_name, "role": "user"}  # Добавляем нового пользователя
    bot.send_message(user_id, "Привет! Я твой бот. Чем могу помочь?", reply_markup=main_menu())

# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Список команд")
    item2 = types.KeyboardButton("Информация")
    markup.add(item1, item2)
    return markup

# Хендлер для команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Список команд:\n/start - Начать\n/help - Помощь\n/commands - Доступные команды")

# Хендлер для команды /commands
@bot.message_handler(commands=['commands'])
def send_commands(message):
    bot.send_message(message.chat.id, "Вот доступные команды:\n/start - Запуск\n/help - Справка\n/admin - Админка")

# Хендлер для команды /admin (доступна только администраторам)
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.chat.id in admin_ids:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Просмотр статистики")
        item2 = types.KeyboardButton("Управление пользователями")
        item3 = types.KeyboardButton("Выход из админки")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Добро пожаловать в админку", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к админке.")

# Хендлер для кнопок в админке
@bot.message_handler(func=lambda message: message.text in ["Просмотр статистики", "Управление пользователями", "Выход из админки"])
def admin_actions(message):
    if message.text == "Просмотр статистики":
        # Пример статистики
        bot.send_message(message.chat.id, f"Количество пользователей: {len(user_data)}")
    elif message.text == "Управление пользователями":
        bot.send_message(message.chat.id, "Управление пользователями: [будет реализовано]")
    elif message.text == "Выход из админки":
        bot.send_message(message.chat.id, "Выход из админки.", reply_markup=main_menu())

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Вы написали: {message.text}")

# Запуск бота
bot.polling()
