import sqlite3
import re

welcome = "Приветствую! Добро пожаловать в помощника по здоровью и поддержке при эпилепсии. " \
          "Я здесь, чтобы помочь вам фиксировать приступы эпилепсии и напоминать о важности приема лекарств. " \
          "С вашей помощью мы сможем создать расписание приема таблеток и записать данные о приступах для более эффективного управления здоровьем. " \
          "Дальше вам нужно будет заполнить небольшую анкету."

def check_for_exist(message):
    chat_id = message.chat.id
    connection = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_info WHERE id = ?", (chat_id,))
    user_record = cursor.fetchone()
    if user_record is None:
        cursor.execute("INSERT INTO user_info (id) VALUES (?)", (chat_id,))

    connection.commit()
    connection.close()

def ask_name(message, bot_ex):
    chat_id = message.chat.id
    bot_ex.send_message(chat_id, welcome)

    bot_ex.send_message(chat_id, 'Как я могу к вам обращаться?')
    bot_ex.register_next_step_handler(message, lambda msg: save_name(msg, bot_ex))

def save_name(message, bot_ex):
    chat_id = message.chat.id
    connection = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE user_info SET name_of_patient = ? WHERE id = ?', (message.text, chat_id))
    connection.commit()
    connection.close()
    ask_timezone(message, bot_ex)

def ask_timezone(message, bot_ex):

    chat_id = message.chat.id
    bot_ex.send_message(chat_id, 'Какой у вас часовой пояс? (опционально, если вы хотите подключить уведомления)')
    bot_ex.register_next_step_handler(message, lambda msg: save_timezone(msg, bot_ex))

def save_timezone(message, bot_ex):
    chat_id = message.chat.id
    pattern = r'^[+-]\d{1,2}$'
    timezone = message.text.strip()
    if re.match(pattern, timezone):
        connection = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
        cursor = connection.cursor()
        cursor.execute('UPDATE user_info SET timezone_utc = ? WHERE id = ?', (message.text.strip(), chat_id))
        connection.commit()
        connection.close()
        ask_about_drug(message, bot_ex)
    else:
        bot_ex.send_message(chat_id, 'Неправильный формат. Введите часовой пояс в формате UTC, GMT. Например: +7 или +3')
        bot_ex.register_next_step_handler(message, lambda msg: save_timezone(msg, bot_ex))


def ask_about_drug(message, bot_ex):
    chat_id = message.chat.id
    bot_ex.send_message(chat_id, 'Какой/какие препараты принимаете?')
    bot_ex.register_next_step_handler(message, lambda msg: save_info_about_drug(msg, bot_ex))

def save_info_about_drug(message, bot_ex):
    chat_id = message.chat.id
    connection = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO user_drugs (drug_name, user_id) VALUES (?,?)', (message.text, chat_id))
    connection.commit()
    connection.close()
    bot_ex.send_message(chat_id, "Вы заполнили анкету. Теперь вы можете фиксировать приступы, нажав на кнопку 'Зафиксировать'")


# def is_questionnaire_completed(user_id):
#     connection = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM user_info WHERE id = ?", (user_id,))
#     data = cursor.fetchone()
#     connection.close()
#     return bool(data)