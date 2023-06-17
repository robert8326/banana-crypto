import requests

from config import TOKEN, API_BASE_URL
from telebot import TeleBot, types

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = requests.get(API_BASE_URL + f'user/telegram/{message.from_user.id}/')
    if response.status_code == 200:
        bot.register_next_step_handler(message, choice_button)
    elif response.status_code == 404:
        bot.register_next_step_handler(message, login)


def choice_button(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_list = types.KeyboardButton('/tasks_list')
    btn_create = types.KeyboardButton('/task_create')
    markup.add(btn_list, btn_create)
    bot.send_message(message.chat.id, "Выберите меню:", reply_markup=markup)


@bot.message_handler(commands=['task_create'])
def get_header(message):
    bot.reply_to(message, 'Введите заголовок новой задачи:')
    bot.register_next_step_handler(message, get_description)


def get_description(message):
    data = {
        'header': message.text
    }
    bot.reply_to(message, 'Введите описание новой задачи:')
    bot.register_next_step_handler(message, create_task, data=data)


def create_task(message, *args, **kwargs):
    kwargs['data']['description'] = message.text
    kwargs['data']['telegram_id'] = message.chat.id
    response = requests.post(API_BASE_URL + 'task/task/', data=kwargs['data'])
    if response.status_code == 201:
        bot.reply_to(message, f'Задача создана успешно!')
    else:
        bot.reply_to(message, f'При создании задачи возникло ошибка!')


@bot.message_handler(commands=['tasks_list'])
def handle_list(message):
    tasks = requests.get(API_BASE_URL + 'task/task/', params={'telegram_id': message.from_user.id})
    task_list = tasks.json()
    if task_list:
        for task in task_list:
            bot.send_message(
                message.chat.id,
                f'<b>Заголовок</b>: {task.get("header")} \n'
                f'<b>Описание</b>: {task.get("description")} \n'
                f'<b>Выполнено</b>: {task.get("completed")}',
                parse_mode='html'
            )
    else:
        bot.send_message(message.chat.id, 'Список задач пуст.')


def login(message):
    bot.reply_to(message, 'Введите username из веб приложения')
    bot.register_next_step_handler(message, get_username)


def get_username(message):
    data = {
        'username': message.text,
    }
    bot.reply_to(message, 'Введите password из веб приложения')
    bot.register_next_step_handler(message, get_password, data=data)


def get_password(message, *args, **kwargs):
    kwargs['data']['password'] = message.text
    kwargs['data']['telegram_id'] = message.chat.id
    response = requests.post(API_BASE_URL + 'user/telegram/login/', data=kwargs['data'])
    if response.status_code == 200:
        bot.reply_to(message, 'Чтобы продолжить, введите команду /start.')
    else:
        bot.send_message(message.chat.id,
                         f'Вы должны зарегистрироваться на сайте {API_BASE_URL}user/register/. \n'
                         f'После регистрации нажмите команду /start'
                         )


bot.infinity_polling()
