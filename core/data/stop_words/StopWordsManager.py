import os


class StopWordsManager():
    """
    Extracts specific word lists for main processing.
    """

    def get_redundant_words(self, lang):
        redundant_words = []
        if lang == 'ru':
            abs_path = os.path.abspath("data/stop_words/redundant/russian")
            redundant_words_dir_path = open(abs_path, 'r', encoding='utf-8')
            redundant_words = redundant_words_dir_path.read().split("\n")
        elif lang == 'eng':
            abs_path = os.path.abspath("data/stop_words/redundant/english")
            redundant_words_dir_path = open(abs_path, 'r', encoding='utf-8')
            redundant_words = redundant_words_dir_path.read().split("\n")
        return redundant_words

    def get_unclear_words(self, lang):
        unclear_words = []
        if lang == 'ru':
            pass
        elif lang == 'eng':
            pass
