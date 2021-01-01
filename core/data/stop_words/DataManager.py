import os


class DataManager():

    def get_redundant_words(self):
        abs_path = os.path.abspath("data/stop_words/redundant/russian")

        redundant_words_dir_path = open(abs_path, 'r', encoding='utf-8')
        print(redundant_words_dir_path.read())
        return redundant_words_dir_path.read()