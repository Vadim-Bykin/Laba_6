from itertools import combinations
from random import randint

# Функция подбора команд в соответствии с ограничениямми:
def select_commands(prof_count, jun_count):
    selected_commands = []
    for prof in combinations(profs, prof_count):
        for jun in combinations(juns, jun_count):
            cur_command = prof + jun
            cur_score = 0
            for item in cur_command:
                cur_score += int(item['score'])
            selected_commands.append([cur_command, cur_score, prof_count, jun_count])

    return selected_commands

# Функция подбора лучшей команды, учитывая ограничения (целевая функция):
def select_best_commands(command_list):
    max_score = 0
    best_commands = []
    for cur_command in command_list:
        if cur_command[1] > max_score:
            max_score = cur_command[1]

    for cur_command in command_list:
        if cur_command[1] == max_score:
            best_commands.append(cur_command)

    return best_commands

COUNT = 4  # Количество игроков в команде

JUN_MIN_SCORE = 0
JUN_MAX_SCORE = 1000

PROF_MIN_SCORE = 2400
PROF_MAX_SCORE = 2900

# Для наглядности - имена профессионалов начинаются на П
# Имена любителей - начинаются на Л
# score - рейтинг
profs = [{'name': 'Пётр', 'score': randint(PROF_MIN_SCORE, PROF_MAX_SCORE)},
         {'name': 'Павел', 'score': randint(PROF_MIN_SCORE, PROF_MAX_SCORE)},
         {'name': 'Платон', 'score': randint(PROF_MIN_SCORE, PROF_MAX_SCORE)},
         {'name': 'Персей', 'score': randint(PROF_MIN_SCORE, PROF_MAX_SCORE)},
         {'name': 'Прохор', 'score': randint(PROF_MIN_SCORE, PROF_MAX_SCORE)}]  # группа профессионалов
juns = [{'name': 'Леонид', 'score': randint(JUN_MIN_SCORE, JUN_MAX_SCORE)},
        {'name': 'Леонард', 'score': randint(JUN_MIN_SCORE, JUN_MAX_SCORE)},
        {'name': 'Лазарь', 'score': randint(JUN_MIN_SCORE, JUN_MAX_SCORE)},
        {'name': 'Лев', 'score': randint(JUN_MIN_SCORE, JUN_MAX_SCORE)},
        {'name': 'Лаврентий', 'score': randint(JUN_MIN_SCORE, JUN_MAX_SCORE)}]  # группа любителей


# Формируем список из всех возможных комбнаций и считаем одновременно рейтинг команды и количество профессионалов и любителей в команде
# Список игроков, рейтинг команды, кол-во профессионалов, кол-во любителей
commands = []
for i in range(COUNT + 1):
    for prof in combinations(profs, i):
        for jun in combinations(juns, COUNT - i):
            cur_command = prof + jun
            cur_score = 0
            for item in cur_command:
                cur_score += int(item['score'])
            commands.append([cur_command, cur_score, i, COUNT - i])

# Первая часть вывода - вывод всех возможных вариантов команд
k = 0
print('-' * 60)
print("Все возможные наборы команд: \n")
for command in commands:
    k += 1
    print(k, '|',
        f"{command[0][0]['name']} ({command[0][0]['score']}) {command[0][1]['name']} ({command[0][1]['score']}) "
        f"{command[0][2]['name']} ({command[0][2]['score']}) {command[0][3]['name']} {command[0][3]['score']}) - {command[1]}")
    print(f"Количество профессионалов - {command[2]}, количество любителей - {command[3]}\n")


# Вторая часть вывода - вывод команд учитывая ограничения
c = 0
prof_count = 1  # количество профессионалов в команде
jun_count = 3  # количество любителей в команде
selected_commands = select_commands(prof_count, jun_count)
print('-' * 80)
print(f'Все команды, удовлетворяющие условиям ({prof_count} профессионал(-а/-ов) и {jun_count} любитель(-я)):')
if len(selected_commands) != 0:
    print('Порядковый номер команды, cостав игроков, общий рейтинг команды \n')
    for command in selected_commands:
        c += 1
        print(c, '|', command[0][0]['name'], command[0][1]['name'], command[0][2]['name'], command[0][3]['name'], '-', command[1])
else:
    print("Команд, удовлетворяющих условиям не найдено")

# Третья часть вывода - вывод наилучшей команды (наибольшее количество очков)
best_commands = select_best_commands(selected_commands)
print('-' * 50)
if len(best_commands) != 0:
    print('Самые лучшие команды:')
    print('Состав игроков, общий рейтинг команды \n')
    for command in best_commands:
        print(command[0][0]['name'], command[0][1]['name'], command[0][2]['name'], command[0][3]['name'], '-', command[1])
    print('-' * 50)
