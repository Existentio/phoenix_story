import os


class StopWordsManager():

    def get_redundant_words(self):
        abs_path = os.path.abspath("data/stop_words/redundant/russian")

        redundant_words_dir_path = open(abs_path, 'r', encoding='utf-8')
        redundant_words = redundant_words_dir_path.read().split("\n")
        return redundant_words
