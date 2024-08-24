import io
import sqlite3
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

def year_count_graph(message, bot_ex):
    chat_id = message.chat.id
    connection = sqlite3.connect("D:/Programming/test1/databases/tg_bot_database.db")
    cursor = connection.cursor()
    query = 'SELECT attack_date, count_of_attacks FROM epilepsy_attacks WHERE user_id = ? ORDER BY attack_date'
    cursor.execute(query, (chat_id,))
    data = cursor.fetchall()

    monthly_attacks = defaultdict(int)
    for entry in data:
        date_str = entry[0]
        count_attacks = int(entry[1])

        date = datetime.strptime(date_str, "%Y-%m-%d")
        monthly_attacks[date.month] += count_attacks

    months = range(1, 13)
    count_attacks = [monthly_attacks[month] for month in months]

    plt.figure(figsize=(10,6))
    plt.bar(months, count_attacks)
    plt.xlabel("Месяц")
    plt.ylabel("Количество приступов")
    plt.title("Количество приступов по месяцам в течение года ")
    plt.xticks(months)
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    bot_ex.send_photo(message.chat.id, buffer.getvalue())

    connection.close()

