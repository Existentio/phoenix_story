# a = [1, 2, 3, 4]
# b = [4, 2, 7, 8]
#
#
# set_a = set(a)
# set_b = set(b)
#
#
# print(set_a.intersection(set_b))
#
#
import re

from core.data.stop_words.StopWordsManager import StopWordsManager


a = 400
b = 400
print(id(a) == id(b))

print(hex(12345))


query = 'я думаю это что-то интересное'
stopwords = StopWordsManager().get_redundant_words()
resultwords = [word for word in re.split("\W+", query) if word.lower() not in stopwords]

result = ''

for word in re.split("\W+", query):
    if word.lower() not in stopwords:
        print(word)
        result += word + " "

print(result)
