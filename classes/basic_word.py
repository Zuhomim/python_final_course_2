class BasicWord:
    """Класс, имеющий поля:
- исходное слово,
- набор допустимых подслов из этого слова"""

    def __init__(self, basic_word, word_list):
        self.basic_word = basic_word
        self.word_list = word_list

    def __repr__(self):
        return f'BasicWord("{self.basic_word}", "{self.word_list}")'

    def check_input_word(self, word):
        """проверяет введенное слово в списке допустимых подслов (вернет bool)"""
        return word in self.word_list

    def count_words(self):
        """подсчет количества подслов"""
        return len(self.word_list)
