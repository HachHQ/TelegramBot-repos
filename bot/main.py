#import matplotlib.pyplot as plt
import user_bio_info
from TOKEN import token
import telebot
from handlers import ask_date_handler, save_user_chat_id
from graph_render_commands import year_count_graph

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_bio_info.check_for_exist(message)
    user_bio_info.ask_name(message, bot)

@bot.message_handler(commands=['fix_epilepsy_attack'])
def fix_attack(message):
    save_user_chat_id(message)
    ask_date_handler(message, bot)

@bot.message_handler(commands=['year_count_gist'])
def show_gist(message):
    year_count_graph(message, bot)

if __name__ == '__main__':
    bot.infinity_polling()