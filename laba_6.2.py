from itertools import combinations
from random import randint

COUNT = 4  # Количество игроков в команде

JUN_MIN_SCORE = 0
JUN_MAX_SCORE = 500

PROF_MIN_SCORE = 2200
PROF_MAX_SCORE = 2900

# Для наглядности - имена профессионалов начинаются на П
# Имена любителей - начинаются на Л
# score - рейтинг игрока
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

k = 0
print('-' * 75)
print("Все возможные наборы команд: \n")
for command in commands:
    k += 1
    print(k, '|',
        f"{command[0][0]['name']} ({command[0][0]['score']}) {command[0][1]['name']} ({command[0][1]['score']}) "
        f"{command[0][2]['name']} ({command[0][2]['score']}) {command[0][3]['name']} ({command[0][3]['score']}) - {command[1]}")
    print(f"Количество профессионалов - {command[2]}, количество любителей - {command[3]}\n")


# Функция подбора команды в соответствии с ограничениями
def select_commands(command_list, prof_count, jun_count):
    selected_commands = []
    for command in command_list:
        if command[2] < prof_count:
            continue
        elif command[3] < jun_count:
            continue

        selected_commands.append(command)

    return selected_commands

# Функция подбора лучшей команды, учитывая ограничения
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

c = 0
prof_count = 2  # количество профессионалов в команде
jun_count = 2  # количество любителей в команде
selected_commands = select_commands(commands, prof_count, jun_count)
print('-' * 90)
print(f'Все команды, удовлетворяющие ограничениям (не менее {prof_count} профессионала(ов) и не менее {jun_count} любителя(ей)):')
if len(selected_commands) != 0:
    print('Порядковый номер команды, состав игроков, общий рейтинг команды \n')
    for command in selected_commands:
        c += 1
        print(c, '|', command[0][0]['name'], command[0][1]['name'], command[0][2]['name'], command[0][3]['name'], '-', command[1])
else:
    print("Команд, удовлетворяющих условиям не найдено")

best_commands = select_best_commands(selected_commands)
print('-' * 50)
if len(best_commands) != 0:
    print('\nСамая(ые) лучшая(ые) команда(ы):')
    print('Состав игроков, общий рейтинг команды \n')
    for command in best_commands:
        print(command[0][0]['name'], command[0][1]['name'], command[0][2]['name'], command[0][3]['name'], '-', command[1])
    print('-' * 50)