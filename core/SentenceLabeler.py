import string

from core.DefaultLanguageDefiner import DefaultLanguageDefiner
from core.data.StopWordsManager import StopWordsManager

# req_sample = '1. According to 1.2.3.4 system must .. do it 20 times,  2.3.3.5.6.643 and it should take <= 0.5 seconds.'
req_sample = '1. Я, Мр. Смит, думаю , что согласно п. 1.2.3.4 система система иногда должна делать и ?. .. ,,,  выполнив операцию 0..10 или 20 раз, должно быть ясно, что в п. 2.3.3.5.6.643 считаю есть ошибка, и это должно занимать <= 0.5 секунд. '

numbers = [str(x) for x in list(range(0, 100))]

punctuation_marks = string.punctuation

# label for sentence element
label_req_id = '[REQ_ID]'
label_uml_modifier = '[UML_MULTIPLICITY]'
label_typo = '[TYPO]'


class SentenceLabeler:
    """Labels sentence parts."""

    def __init__(self, sentence):
        self.sentence = sentence
        self.swm = StopWordsManager()
        self.lang = DefaultLanguageDefiner(self.sentence).define_default_language()

    def define_sentence_labels(self):
        sentence_with_labels = ''
        cnt_ext = 0

        # todo algo on 2 methods: 1 should get only useful parts like uml multiplicities, main sentence, etc.
        #  and 2nd one should operate with trash

        for x in range(len(self.sentence.split())):
            for y in req_sample.split()[x]:
                if y == '.':
                    cnt_ext += 1
            try:
                if cnt_ext == 1:
                    if (self.sentence.split()[x + 1] in self.swm.get_time_units(self.lang)) \
                            or (self.sentence.split()[x + 1][:len(self.sentence.split()[x + 1]) - 1]
                                in self.swm.get_time_units(self.lang)):
                        sentence_with_labels += self.sentence.split()[x] + ' '
                        print('it is time unit: ', self.sentence.split()[x + 1])
                    for y in range(len(self.sentence.split()[x])):
                        if self.sentence.split()[x][y] in numbers:
                            sentence_with_labels += label_req_id
                            print('it is req id: ', self.sentence.split()[x])
                            break
                        if self.sentence.split()[x][y] in punctuation_marks \
                                and self.sentence.split()[x][y - 1] in punctuation_marks:
                            sentence_with_labels += self.sentence.split()[x] + ' '
                            print('it is typo or smth else, cnt_ext == 1: ', self.sentence.split()[x])
                            break
                        else:
                            sentence_with_labels += self.sentence.split()[x] + ' '
                            break
                    cnt_ext = 0
            except IndexError:
                print('got index error', self.sentence.split()[x])
                pass
            if cnt_ext == 2:
                for y in range(len(self.sentence.split()[x])):
                    if self.sentence.split()[x][y] in numbers \
                            and self.sentence.split()[x][y - 1] in punctuation_marks \
                            and self.sentence.split()[x][y - 2] in punctuation_marks:
                        sentence_with_labels += self.sentence.split()[x] + ' '
                        print('it is uml modifier: ', self.sentence.split()[x])
                        break
                    if self.sentence.split()[x][y] not in numbers \
                            and self.sentence.split()[x][y - 1] in punctuation_marks \
                            and self.sentence.split()[x][y - 2] in punctuation_marks:
                        sentence_with_labels += self.sentence.split()[x] + ' '
                        print('it is a typo cnt_ext == 2: ', self.sentence.split()[x])
                        break
                cnt_ext = 0
            elif cnt_ext > 2:
                cnt_int = 0
                for y in range(len(self.sentence.split()[x])):
                    if self.sentence.split()[x][y] in numbers:
                        cnt_int += 1
                    if cnt_int == 1 and self.sentence.split()[x][y - 1] in punctuation_marks:
                        sentence_with_labels += self.sentence.split()[x] + ' '
                        print('it is typo: ', self.sentence.split()[x])
                        break
                    if cnt_int == 1:
                        sentence_with_labels += self.sentence.split()[x] + label_req_id + ' '
                        print('it is req id: ', self.sentence.split()[x])
                        break
                    cnt_ext = 0
            else:
                sentence_with_labels += self.sentence.split()[x] + ' '
            if len(self.sentence.split()[x]) == 1 and self.sentence.split()[x] == '.':
                print('it is end sentence dot: ', self.sentence.split()[x])
            # cnt_ext = 0
        return sentence_with_labels

    def bind_sentence_words_with_ids(self):
        dict_labeled_str = {}

        labeled_str_splitted = self.define_sentence_labels().split()

        for x in labeled_str_splitted:
            dict_labeled_str[labeled_str_splitted.index(x)] = x

        print(dict_labeled_str)
        return dict_labeled_str

    def detach_main_sentence(self):
        main_sentence_without_req_id = ''

        dict_labeled_str = self.bind_sentence_words_with_ids()

        for x in dict_labeled_str:
            if dict_labeled_str[x].find(label_req_id) != -1:
                print(dict_labeled_str[x])
                pass
            # elif dict_labeled_str[x].find(label_uml_modifier) != -1:
            #     print(dict_labeled_str[x])
            #     pass
            else:
                main_sentence_without_req_id += dict_labeled_str[x] + ' '
        #
        print(main_sentence_without_req_id)
        return main_sentence_without_req_id


sl = SentenceLabeler(req_sample)

print(sl.define_sentence_labels())

print('====\n')
sl.detach_main_sentence()
