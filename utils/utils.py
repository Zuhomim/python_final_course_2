import requests
import random


def load_random_word(url, basic_word_class):
    """получает список слов с внешнего ресурса,
- выбирает случайное слово,
- создает экземпляр класса `BasicWord`,
- возвращает этот экземпляр."""
    response = requests.get(url)
    response_json = response.json()

    random_word = random.choice(response_json)
    random_word_name = random_word['word']
    sub_words = random_word['subwords']

    new_word = basic_word_class(random_word_name, sub_words)

    return new_word


def choose_ending_word(count_):
    """Вычисляет нужное окончание существительного, относящегося к числительному"""
    ending = ''
    if count_ % 10 == 1:
        ending = 'о'
    if count_ % 10 in [2, 3, 4]:
        ending = 'а'

    return ending
