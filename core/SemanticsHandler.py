from core.SentenceLabeler import SentenceLabeler
from core.DefaultLanguageDefiner import DefaultLanguageDefiner


class SemanticsHandler:
    sentence_labeler = SentenceLabeler()
    main_sentence = SentenceLabeler.detach_main_sentence(sentence_labeler)

    print('\nmain sentence: ', main_sentence)

    t = DefaultLanguageDefiner.define_default_language(DefaultLanguageDefiner('ss'))

