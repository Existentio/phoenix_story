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

test_sentence = 'it should take no more'

# it   should   t  a  k  e
# 01 2 345678 9 10 11 12 13
for x in range(len(test_sentence)):
    if test_sentence[x] == ' ':
        print(x)
        print('here is whitespace')

    print(test_sentence[x])

t = {1: 's', 2: 't'}
s = []

z = {}
counter = 0
for x in t:
    counter += 1
    z[counter] = t.values()

print(z)
