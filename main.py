from utils.utils import load_random_word, choose_ending_word
from classes.player import Player
from classes.basic_word import BasicWord

# Адрес с json данными для программы
url = "https://www.jsonkeeper.com/b/IPLY"
# Команда для остановки программы
stop = "stop"
# Имя пользователя
username = input(f'Введите имя игрока\n')
# Создание экземпляра класса пользователя
player = Player(username, [])

print(f'Привет, {username}')

random_word = load_random_word(url, BasicWord)

print(f'Составьте {random_word.count_words()} слов из слова {random_word.basic_word.upper()}')
print(f'''Слова должны быть не короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите команду {stop}
''')
print(f'Поехали, Ваше первое слово?')

# Основной цикл программы, заканчивающийся командой stop либо разгадкой всех слов, к-ые можно составить
while True:
    player_word = input()
    if player_word.lower() == stop:
        break
    if len(player_word) < 3:
        print('Слишком короткое слово')
        continue
    if player_word.lower() not in random_word.word_list:
        print('неверно')
        continue
    if player.check_word(player_word):
        print('слово уже использовано')
        continue

    player.add_word(player_word)
    print('верно')

    if len(player.user_words) == random_word.count_words():
        break

# Вывод статистики (кол-во угоаданных слов)
print(f'Игра завершена. Вы угадали {len(player.user_words)} слов{choose_ending_word(len(player.user_words))}!')
