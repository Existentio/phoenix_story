# minimal potential length of requirement

test_text = 'При первом открытии а п.1.23приложения "Х" должен появляться новый экран. ' \
            '1.1 Если экран успешно открылся, то начнет загружаться новая страница. ' \
            '1.2 Если появилась ошибка, то стоит отобразить юзеру модальное окно с текстом ошибки.' \
            'Цвет модального окна: #232832.' \
            '1.2.1 В модальном окне при нажатии на "Отмена" выполнение перейдет к п. 1.1. '


# todo for future functionality: add notification if requirement
#  is more than X symbols, offer to divide into 2 reqs [i.e. if more than 90 symbols]

# todo implement main algo for dividing input name to N sentences

# todo divided sentences should have id , because of further sequential or parallel processing
#  [labeling -> semantics handling -> structure handling, etc.


class ReqSeparator:
    """Separates input name to N sentences for further cleaning and improving each requirement."""

    sentences = []

    def __init__(self, text):
        print('\n===============')
        self.text = text.strip()

    def get_text(self):
        return self.text

    def divide_reqs(self):
        l_chr_index = 0
        r_chr_index = 90
        max_req_len = 90



        for x in self.text.split():
            print(len(x))


        while r_chr_index != (len(self.text) - 1):
            # print(r_chr_index)
            # print(len(self.name[l_chr_index:r_chr_index]))

            if len(self.text[l_chr_index:r_chr_index]) >= max_req_len:
                # print(self.name[l_chr_index:r_chr_index].split())
                self.sentences.append(self.text[l_chr_index:r_chr_index])
                r_chr_index += r_chr_index
                l_chr_index += r_chr_index
                print(r_chr_index)



        print(self.sentences)


ReqSeparator(test_text).divide_reqs()
