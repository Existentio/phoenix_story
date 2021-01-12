import os


class StopWordsManager:
    """Extracts specific word lists for main processing."""

    def get_redundant_words(self, lang):
        redundant_words = []
        if lang == 'ru':
            abs_path = os.path.abspath("data/stop_words/redundant/russian")
            dir_path = open(abs_path, 'r', encoding='utf-8')
            redundant_words = dir_path.read().split("\n")
        elif lang == 'eng':
            abs_path = os.path.abspath("data/stop_words/redundant/english")
            dir_path = open(abs_path, 'r', encoding='utf-8')
            redundant_words = dir_path.read().split("\n")
        return redundant_words

    def get_unclear_words(self, lang):
        unclear_words = []
        if lang == 'ru':
            abs_path = os.path.abspath("data/stop_words/unclear/russian")
            dir_path = open(abs_path, 'r', encoding='utf-8')
            unclear_words = dir_path.read().split("\n")
        elif lang == 'eng':
            abs_path = os.path.abspath("data/stop_words/unclear/english")
            dir_path = open(abs_path, 'r', encoding='utf-8')
            unclear_words = dir_path.read().split("\n")
        return unclear_words

    def get_time_units(self, lang):
        time_units = []
        if lang == 'ru':
            abs_path = os.path.abspath("data/stop_words/time_unit/russian")
            dir_path = open(abs_path, 'r', encoding='utf-8')
            time_units = dir_path.read().split("\n")
        elif lang == 'eng':
            abs_path = os.path.abspath("data/stop_words/time_unit/english")
            dir_path = open(abs_path, 'r', encoding='utf-8')
            time_units = dir_path.read().split("\n")
        return time_units
