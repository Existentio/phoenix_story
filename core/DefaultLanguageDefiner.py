"""

Helps to identify natural language by default for further semantics processing

"""

eng_alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
ru_alphabet = [chr(x) for x in range(ord('а'), ord('я') + 1)]
ru_alphabet += 'ё'

class DefaultLanguageDefiner:

    def __init__(self, sentence):
        self.sentence = sentence.replace(' ', '')

    def define_default_language(self):
        # print('============\ninput sentence: ' + self.sentence)
        counter = 0

        for x in self.sentence:
            if x in eng_alphabet:
                counter += 1

        eng_words_percentage = counter / len(self.sentence)
        print('count of eng words: ' + str(counter))
        print('eng words percentage: ' + str(eng_words_percentage))

        return 'eng' if eng_words_percentage > 0.5 else 'ru'


