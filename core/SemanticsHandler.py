from core.SentenceLabeler import SentenceLabeler
from core.DefaultLanguageDefiner import DefaultLanguageDefiner


class SemanticsHandler:
    sentence_labeler = SentenceLabeler()
    main_sentence = SentenceLabeler.detach_main_sentence(sentence_labeler)

    print('\nmain sentence: ', main_sentence)

    default_language = DefaultLanguageDefiner(main_sentence)
    print(default_language.define_default_language())

    def define_language_rules(self, default_language):
        self.define_ru_rules() if default_language == 'ru' else self.define_eng_rules()

    def define_eng_rules(self):
        print('eng rules has been defined')

    def define_ru_rules(self):
        print('ru rules has been defined')

    define_ru_rules()

    define_language_rules(default_language)
