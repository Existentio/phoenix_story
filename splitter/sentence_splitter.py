"""
Split sentences of your pseudo requirements for further processing

"""


# list of simple numbers [convert list of int to list of str]
simple_numbers = [str(x) for x in list(range(0, 10))]

# punctuation marks
punctuation_marks = [',', '.', ':', ';']

#
starters = ['Мр.']

# provide a label for element of sentence
label_req_id_start = 'req_id_start'
label_req_id_end = 'req_id_end'
label_req_main_sentence_start = ''
label_req_main_sentence_end = ''

# sentence with labels for further processing
sentence_with_labels = ''


# minimal potential length of requirement
min_req_len = 8


test_req_1 = 'При первом открытии приложения "Х" должен появляться новый экран. ' \
             '1.1 Если экран успешно открылся, то начнет загружаться новая страница. ' \
             '1.2 Если появилась ошибка, то стоит отобразить юзеру модальное окно с текстом ошибки.' \
             'Цвет модального окна: #232832.' \
             '1.2.1 В модальном окне при нажатии на "Отмена" выполнение перейдет к п. 1.1. '

# todo for future functionality: add notification if requirement
#  is more than X symbols [offer to divide into 2 reqs and so on]

print(simple_numbers)


def divide_req(req: str):
    # todo need req_sample statement here to divide new sentence from in-sentence words like "Mr. Smith",
    #  or req. № 1.2.1
    tmp = req.split('.')

    print('===INPUT===')
    print(tmp)
    print('\n')

    reqs = []
    for x in tmp:
        if len(x) > min_req_len:
            reqs.append(x)
            print(x)
        else:
            continue

    print('\n===OUTPUT===')
    print('len reqs: ' + str(len(reqs)))
    print(reqs)


print(divide_req(test_req_1))

print('===')

req_sample = '1.2.3.4 you must do this 2.3'

# todo need to add req identifiers to list with seperated value i.e. whitespace and slice it to str
#  to make sure that req like "1.2 User can press the button and executes running 1.3" will be ok



idx = -1

sentence_with_labels += label_req_id_start

for symb in req_sample:
    # if symb in simple_numbers:
    # print(req_sample.index(symb))

    if (req_sample[(req_sample.index(symb) + idx)]) in punctuation_marks or simple_numbers:
        if req_sample[(req_sample.index(symb))] == ' ':
            sentence_with_labels+=label_req_id_end
            break
        else:
            idx = (idx + 1)
            print('here is punctuation mark or simple number, moving next')
            print(symb)
            sentence_with_labels+=(req_sample[(req_sample.index(symb))])

# else:
#     'bad algorithm'

print(sentence_with_labels)
