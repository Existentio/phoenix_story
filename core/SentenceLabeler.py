# req_sample = '1. According to 1.2.3.4 system must .. do it 20 times,  2.3.3.5.6.643 and it should take <= 0.5 seconds.'
from core.data.StopWordsManager import StopWordsManager

req_sample = '1. Я, Мр. Смит, думаю , что согласно п. 1.2.3.4 система система иногда должна делать .. и выполнив операцию 20 раз, должно быть ясно, что в п. 2.3.3.5.6.643 считаю есть ошибка, и это должно занимать <= 0.5 секунд. '

# list of simple numbers [convert list of int to list of sentence]
numbers = [str(x) for x in list(range(0, 100))]

punctuation_marks = [',', '.', ':', ';']

starters = ['Мр.', 'Мисс.']

# label for sentence element
label_req_id = '[REQ_ID]'
label_req_main_sentence_start = '[MAIN_START]'
label_req_main_sentence_end = '[MAIN_END]'
label_uml_modifier = '[UML_MODIFIER]'

time_units = ['секунд', 'минут', 'час', 'день']


class SentenceLabeler:
    """Labels sentence parts."""

    # todo need label sentence for separating req identifiers from words

    def __init__(self):
        self.swm = StopWordsManager()

    def define_sentence_labels(self):
        sentence_with_labels = ''
        cnt_ext = 0

        for x in range(len(req_sample.split())):
            for y in req_sample.split()[x]:
                if y == '.':
                    cnt_ext += 1
            try:
                cnt_int = 0
                if cnt_ext == 1:
                    if (req_sample.split()[x + 1] in time_units) \
                            or (req_sample.split()[x + 1][:len(req_sample.split()[x + 1]) - 1] in time_units):
                        print('it is time unit: ', req_sample.split()[x + 1])
                        sentence_with_labels += req_sample.split()[x] + ' '

                    for y in range(len(req_sample.split()[x])):
                        if req_sample.split()[x][y] in numbers:
                            cnt_int += 1
                        if cnt_int == 1:
                            print('it is req id: ', req_sample.split()[x])
                            sentence_with_labels += label_req_id
                            break
                        else:
                            sentence_with_labels += req_sample.split()[x] + ' '
                        cnt_int = 0
                    cnt_ext = 0
            except IndexError:
                print('got index error', req_sample.split()[x])
                pass
            if len(req_sample.split()[x]) == 1 and req_sample.split()[x] == '.':
                print('it is end sentence dot: ', req_sample.split()[x])
            if cnt_ext == 2:
                cnt_int = 0
                for y in range(len(req_sample.split()[x])):
                    if req_sample.split()[x][y] in numbers:
                        cnt_int += 1
                    if cnt_int < 4 and req_sample.split()[x][y] == '.':
                        cnt_int += 1
                    if cnt_int == 4 and req_sample.split()[x][y] in numbers:
                        print('it is uml modifier: ', req_sample.split()[x])
                        sentence_with_labels += req_sample.split()[x] + ' '
                    else:
                        print('it is a typo: ', req_sample.split()[x])
                        sentence_with_labels += req_sample.split()[x] + ' '
                cnt_ext = 0
            elif cnt_ext > 2:
                cnt_int = 0
                for y in range(len(req_sample.split()[x])):
                    if req_sample.split()[x][y] in numbers:
                        cnt_int += 1
                    if cnt_int == 1 and req_sample.split()[x][y - 1] == '.':
                        print('it is typo: ', req_sample.split()[x])
                        sentence_with_labels += req_sample.split()[x] + ' '
                        break
                    if cnt_int == 1:
                        print('it is req id: ', req_sample.split()[x])
                        sentence_with_labels += req_sample.split()[x] + label_req_id + ' '
                        break
                    cnt_ext = 0
            else:
                sentence_with_labels += req_sample.split()[x] + ' '
                print('counter', cnt_ext, req_sample.split()[x])
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
            if dict_labeled_str[x].find(label_req_id) == -1:
                main_sentence_without_req_id += dict_labeled_str[x] + ' '
            else:
                # print(dict_labeled_str[x])
                pass
        #
        print(main_sentence_without_req_id)
        return main_sentence_without_req_id


sl = SentenceLabeler()

# print(sl.define_sentence_labels())

print('====\n')
sl.detach_main_sentence()
