# minimal potential length of requirement
max_req_len = 70

test_req_1 = 'При первом открытии а п.1.23приложения "Х" должен появляться новый экран. ' \
             '1.1 Если экран успешно открылся, то начнет загружаться новая страница. ' \
             '1.2 Если появилась ошибка, то стоит отобразить юзеру модальное окно с текстом ошибки.' \
             'Цвет модального окна: #232832.' \
             '1.2.1 В модальном окне при нажатии на "Отмена" выполнение перейдет к п. 1.1. '


# todo for future functionality: add notification if requirement
#  is more than X symbols [offer to divide into 2 reqs and so on]


def divide_req(req: str):
    pass
