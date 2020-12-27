from core.SentenceLabeler import SentenceLabeler
from core.DefaultLanguageDefiner import DefaultLanguageDefiner


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


semantics_handler = SemanticsHandler()
print(semantics_handler.define_language_rules())
