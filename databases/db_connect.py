import sqlite3

connection = sqlite3.connect('tg_bot_database.db')
cursor = connection.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS user_info (id INTEGER PRIMARY KEY, NAME_OF_PATIENT TEXT, TIMEZONE_UTC TEXT)''')

# cursor.execute('''SELECT attack_date, count_of_attacks FROM epilepsy_attacks WHERE attack_date BETWEEN date('now', '-1 year') AND date('now') AND user_id = 466024868''')

cursor.execute('''SELECT date('now') as date,
                         time('now') as time;''')

# cursor.execute('''INSERT INTO epilepsy_attacks (user_id, attack_date, attack_time, duration_attack_time, count_of_attacks)
# VALUES
#     (466024868, '2022-01-01', '10:30', '15', '5'),
#     (466024868, '2022-02-02', '09:45', '20', '3'),
#     (466024868, '2022-03-03', '14:20', '12', '6'),
#     (466024868, '2022-04-04', '11:55', '18', '4'),
#     (466024868, '2022-05-05', '08:10', '25', '2'),
#     (466024868, '2022-06-06', '13:25', '10', '7'),
#     (466024868, '2022-07-07', '16:40', '30', '1'),
#     (466024868, '2022-08-08', '12:15', '22', '8'),
#     (466024868, '2022-09-09', '07:50', '17', '9'),
#     (466024868, '2022-10-10', '17:05', '14', '5'),
#     (466024868, '2022-11-11', '10:30', '21', '3'),
#     (466024868, '2022-12-12', '09:45', '19', '6'),
#     (466024868, '2022-01-13', '14:20', '13', '4'),
#     (466024868, '2022-02-14', '11:55', '24', '2'),
#     (466024868, '2022-03-15', '08:10', '11', '7'),
#     (466024868, '2022-04-16', '13:25', '28', '1'),
#     (466024868, '2022-05-17', '16:40', '16', '8'),
#     (466024868, '2022-06-18', '12:15', '23', '9'),
#     (466024868, '2022-07-19', '07:50', '20', '5'),
#     (466024868, '2022-08-20', '17:05', '18', '3');
#
# ''')
# cursor.execute("PRAGMA foreign_keys = ON")
# cursor.execute('''
#             CREATE TABLE IF NOT EXISTS user_drugs(
#             drug_id INTEGER PRIMARY KEY,
#             user_id INTEGER,
#             drug_name TEXT,
#             FOREIGN KEY (user_id) REFERENCES user_info (id)
#             )
#             ''')
#cursor.execute("ALTER TABLE user_info ADD epilSELECT epsy_attack TEXT")
#cursor.execute("* FROM user_info")

data = cursor.fetchone()

# for i in data:
print(data)

# cursor.execute('''
#                DELETE FROM epilepsy_attacks
#                '''
# )

connection.commit()
connection.close()