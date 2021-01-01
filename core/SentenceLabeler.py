"""
Labeler parts of your sentence for further processing

"""

# req_sample = '1. According to 1.2.3.4 system must .. do it 20 times,  2.3.3.5.6.643 and it should take <= 0.5 seconds.'
req_sample = '1. Я думаю , согласно п. 1.2.3.4 система должна .. выполнив операцию 20 раз,  2.3.3.5.6.643 и это должно занять <= 0.5 секунд.'

# list of simple numbers [convert list of int to list of sentence]
simple_numbers = [str(x) for x in list(range(0, 100))]

punctuation_marks = [',', '.', ':', ';']

starters = ['Мр.']

# label for sentence element
label_req_id_start = 'REQ_ID_START'
label_req_id_end = 'REQ_ID_END'
label_req_main_sentence_start = 'MAIN_START'
label_req_main_sentence_end = 'MAIN_END'


class SentenceLabeler:

    # todo need to add req identifiers to list with seperated value i.e. whitespace and slice it to sentence
    #  to make sure that req like "1.2 User can press the button and executes running 1.3" will be ok

    # todo need label sentence for separating req identifiers from words

    # todo need take into account that req may be contain smth like this:
    #  "operation should be take no more than 0.5 sec.."

    def define_sentence_labels(self):
        sentence_with_labels = ''
        counter = 0

        for symb in req_sample:
            if (req_sample[(req_sample.index(symb))]) in punctuation_marks:
                print('here is punctuation mark, moving next: ' + symb)
                sentence_with_labels += (req_sample[(req_sample.index(symb))])

            elif (req_sample[(req_sample.index(symb))]) in simple_numbers:
                counter += 2
                print('here is simple number, moving next: ' + symb)
                sentence_with_labels += (req_sample[(req_sample.index(symb))])
            elif (req_sample[(req_sample.index(symb))]) == ' ':
                if counter >= 2:
                    sentence_with_labels += label_req_id_end
                    counter = 0
                sentence_with_labels += (req_sample[(req_sample.index(symb))])
                print('here is whitespace')

            else:
                print('here is sentence character, moving next: ' + symb)
                sentence_with_labels += (req_sample[(req_sample.index(symb))])

        return sentence_with_labels.strip()

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
            if dict_labeled_str[x].find(label_req_id_end) == -1:
                main_sentence_without_req_id += dict_labeled_str[x] + ' '
            else:
                print(dict_labeled_str[x])

        print(main_sentence_without_req_id)
        return main_sentence_without_req_id
