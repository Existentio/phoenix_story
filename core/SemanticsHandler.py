import re

from core.DefaultLanguageDefiner import DefaultLanguageDefiner
from core.SentenceLabeler import SentenceLabeler
from core.data.StopWordsManager import StopWordsManager


class SemanticsHandler:
    """Main class for sentence proccessing and converting sentence to requirement."""

    def __init__(self, sentence):
        print('\n===============Semantics handler initialized===============')
        self.sentence = sentence
        self.requirement = ''
        self.unclear_words = []
        self.swm = StopWordsManager()
        self.default_language = DefaultLanguageDefiner(self.sentence).define_default_language()

    def define_language_rules(self):
        self.define_ru_rules() if self.default_language == 'ru' else self.define_eng_rules()

    def define_eng_rules(self):
        print('eng rules has been defined')

    def define_ru_rules(self):
        print('ru rules has been defined')

    def remove_redundant_words(self):
        redundant_words = self.swm.get_redundant_words(self.default_language)
        for word in self.sentence.split():
            if word.lower() not in redundant_words:
                self.requirement += word + " "
        return self.requirement

    def extract_unclear_words(self):
        unclear_words = self.swm.get_unclear_words(self.default_language)
        for word in self.requirement.split():
            if word.lower() in unclear_words:
                self.unclear_words.append(word)

    def get_unclear_words(self):
        return self.unclear_words


sentence_labeler = SentenceLabeler()
sentence = SentenceLabeler.detach_main_sentence(sentence_labeler)

semantics_handler = SemanticsHandler(sentence)
semantics_handler.define_language_rules()
print(semantics_handler.sentence)
print(semantics_handler.remove_redundant_words())
print(semantics_handler.extract_unclear_words())
print('Неоднозначные слова: ', semantics_handler.get_unclear_words())
