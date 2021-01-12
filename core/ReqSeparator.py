# minimal potential length of requirement
max_req_len = 70

test_req_1 = 'При первом открытии а п.1.23приложения "Х" должен появляться новый экран. ' \
             '1.1 Если экран успешно открылся, то начнет загружаться новая страница. ' \
             '1.2 Если появилась ошибка, то стоит отобразить юзеру модальное окно с текстом ошибки.' \
             'Цвет модального окна: #232832.' \
             '1.2.1 В модальном окне при нажатии на "Отмена" выполнение перейдет к п. 1.1. '


# todo for future functionality: add notification if requirement
#  is more than X symbols, offer to divide into 2 reqs [i.e. if more than 90 symbols]

# todo implement main algo for dividing input text to N sentences

# todo divided sentences should have id , because of further sequential or parallel processing
#  [labeling -> semantics handling -> structure handling, etc.



class ReqSeparator():
    """Separates requirements for cleaning and improving each requirement."""

    def divide_reqs(self):
        pass
