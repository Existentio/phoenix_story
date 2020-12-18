
# minimal potential length of requirement
min_req_len = 8

test_req_1 = 'При первом открытии приложения "Х" должен появляться новый экран. ' \
             '1.1 Если экран успешно открылся, то начнет загружаться новая страница. ' \
             '1.2 Если появилась ошибка, то стоит отобразить юзеру модальное окно с текстом ошибки.' \
             'Цвет модального окна: #232832.' \
             '1.2.1 В модальном окне при нажатии на "Отмена" выполнение перейдет к п. 1.1. '

# todo for future functionality: add notification if requirement
#  is more than X symbols [offer to divide into 2 reqs and so on]



def divide_req(req: str):
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