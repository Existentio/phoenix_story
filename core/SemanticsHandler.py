import re

from core.DefaultLanguageDefiner import DefaultLanguageDefiner
from core.SentenceLabeler import SentenceLabeler
from core.data.stop_words.StopWordsManager import StopWordsManager


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
        redundant_words = StopWordsManager().get_redundant_words()
        result = ''
        print('\n===============')
        for word in re.split(" ", self.main_sentence):
            if word.lower() not in redundant_words:
                result += word + " "
        return result


semantics_handler = SemanticsHandler()
print(semantics_handler.define_language_rules())
print(semantics_handler.remove_redundant_words())
