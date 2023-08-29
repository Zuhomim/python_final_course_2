class Player:
    """Класс пользователя-игрока, имеющий поля:
- имя пользователя,
- список слов, разгаданных пользователем"""

    def __init__(self, username, user_words):
        self.username = username
        self.user_words = user_words

    def __repr__(self):
        return f'Player("{self.username}", "{self.user_words}")'

    def get_words_int(self):
        """получает количество использованных слов (возвращает int);"""
        return len(self.user_words)

    def add_word(self, word):
        """добавляет слова в использованные слова (ничего не возвращает);"""
        self.user_words.append(word)

    def check_word(self, word):
        """проверка использования данного слова до этого (возвращает bool)."""
        return word in self.user_words
