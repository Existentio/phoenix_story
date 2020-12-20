"""

Helps to identify natural language by default for further semantics processing

"""

eng_alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
ru_alphabet = [chr(x) for x in range(ord('а'), ord('я') + 1)]
ru_alphabet += 'ё'


class DefaultLanguageDefiner:
    default_language = 'eng'
    sentence = ''

    def __init__(self, str):
        self.sentence = str

    sentence = sentence.replace(' ', '')

    counter = 0

    for x in sentence:
        if x in eng_alphabet:
            counter += 1

    eng_words_percentage = counter / len(sentence)

    def define_default_language(self):
        return 'eng' if self.eng_words_percentage > 0.5 else 'ru'

    print(eng_words_percentage)
    print(define_default_language())
