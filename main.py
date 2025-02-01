import telebot

# Токен, который вы получили от BotFather
TOKEN = '7752147800:AAGskc5yPs2me4VMU3U2PYMJwz6F3VLQ1DI'

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш нистраторский бот.")

# Функция для обработки команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Это пстой администраторский бот. Используйте команды /start и /help.")

# Функция для добавления администратора
@bot.message_handler(commands=['setadmin'])
def set_admin(message):
    # Проверка, что пользователь является администратором
    if message.from_user.id == 1643330519:
        bot.reply_to(message, "Вы стали администратором!")
    else:
        bot.reply_to(message, "У вас нет прав для выполнения этой команды.")

# Запуск бота
bot.polling()
