import os

from core.SentenceLabeler import SentenceLabeler
from core.DefaultLanguageDefiner import DefaultLanguageDefiner
import pkgutil

from core.data.stop_words.DataManager import DataManager


class SemanticsHandler:
    sentence_labeler = SentenceLabeler()
    main_sentence = SentenceLabeler.detach_main_sentence(sentence_labeler)
    default_language = DefaultLanguageDefiner(main_sentence).define_default_language()

    def define_language_rules(self):
        self.define_ru_rules() if self.default_language == 'ru' else self.define_eng_rules()

    def define_eng_rules(self):
        print('eng rules has been defined')

    def define_ru_rules(self):
        print('ru rules has been defined')

    def remove_redundant_words(self):
        redundant_words = DataManager().get_redundant_words()
        print(redundant_words)



semantics_handler = SemanticsHandler()
print(semantics_handler.define_language_rules())
semantics_handler.remove_redundant_words()