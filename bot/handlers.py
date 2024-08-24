import re

class AttackDataHandler:
    def __init__(self):
        self.data = {}

    def set_user_id(self, user_id):
        self.data['user_id'] = user_id

    def set_date(self, date):
        self.data['date'] = date

    def set_time(self, time):
        self.data['time'] = time

    def set_duration(self, duration):
        self.data['duration'] = duration

    def set_count(self, count):
        self.data['count'] = count

    def insert_into_db(self):
        import sqlite3
        conn = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO epilepsy_attacks (user_id, attack_date, attack_time, duration_attack_time, count_of_attacks) VALUES (?, ?, ?, ?, ?)",
                       (self.data['user_id'], self.data['date'], self.data['time'], self.data['duration'], self.data['count']))
        conn.commit()
        conn.close()

dataHandler = AttackDataHandler()

def save_user_chat_id(message):
    dataHandler.set_user_id(message.chat.id)

def ask_date_handler(message, bot_ex):
    chat_id = message.chat.id
    bot_ex.send_message(chat_id, "Введите дату приступа: (в формате год-месяц-день)")
    bot_ex.register_next_step_handler(message, lambda msg: save_date_of_attack_handler(msg, bot_ex))

def save_date_of_attack_handler(message, bot_ex):
    chat_id = message.chat.id
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    date = message.text.strip()
    if re.match(pattern, date):
        dataHandler.set_date(date)
        ask_time_handler(message, bot_ex)
    else:
        bot_ex.send_message(chat_id, "Введите дату в корректном формате, например: 2003-11-03")
        bot_ex.register_next_step_handler(message, lambda msg: save_date_of_attack_handler(msg, bot_ex))

def ask_time_handler(message, bot_ex):
    chat_id = message.chat.id
    bot_ex.send_message(chat_id, "Введите примерное время приступа: (в 24 часовом формате)")
    bot_ex.register_next_step_handler(message, lambda msg: save_time_of_attack_handler(msg, bot_ex))

def save_time_of_attack_handler(message, bot_ex):
    chat_id = message.chat.id
    pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d$'
    time = message.text.strip()
    if re.match(pattern, time):
        dataHandler.set_time(time)
        ask_duration_handler(message, bot_ex)
    else:
        bot_ex.send_message(chat_id, "Введите время в корректном формате, например 15:45)")
        bot_ex.register_next_step_handler(message, lambda msg: save_time_of_attack_handler(msg, bot_ex))

def ask_duration_handler(message, bot_ex):
    chat_id = message.chat.id
    bot_ex.send_message(chat_id, "Введите примерную продолжительность фазы реабилитации приступа(постиктальная фаза): (в минутах)")
    bot_ex.register_next_step_handler(message, lambda msg: save_duration_of_attack_handler(msg, bot_ex))

def save_duration_of_attack_handler(message, bot_ex):
    chat_id = message.chat.id
    pattern = r'^\d{1,3}$'
    duration = message.text.strip()
    if re.match(pattern, duration):
        dataHandler.set_duration(duration)
        ask_count_handler(message, bot_ex)
    else:
        bot_ex.send_message(chat_id, "Введите время в корректном формате, например 34 или 45)")
        bot_ex.register_next_step_handler(message, lambda msg: save_duration_of_attack_handler(msg, bot_ex))

def ask_count_handler(message, bot_ex):
    chat_id = message.chat.id
    bot_ex.send_message(chat_id, "Введите количество случившихся приступов: (количество)")
    bot_ex.register_next_step_handler(message, lambda msg: save_count_of_attack_handler(msg, bot_ex))

def save_count_of_attack_handler(message, bot_ex):
    chat_id = message.chat.id
    pattern = r'^\d{1,2}$'
    count = message.text.strip()
    if re.match(pattern, count):
        dataHandler.set_count(count)
        dataHandler.insert_into_db()
        bot_ex.send_message(chat_id, "Приступ зафиксирован")
    else:
        bot_ex.send_message(chat_id, "Введите время в корректном формате, например 34 или 45)")
        bot_ex.register_next_step_handler(message, lambda msg: save_count_of_attack_handler(msg, bot_ex))

