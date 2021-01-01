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

# it   should   sentence_labeler  a  k  e
# 01 2 345678 9 10 11 12 13
for x in range(len(test_sentence)):
    if test_sentence[x] == ' ':
        print(x)
        print('here is whitespace')

    print(test_sentence[x])

t = {1: 'main_sentence_without_req_id', 2: 'sentence_labeler'}
s = []

z = {}
counter = 0
for x in t:
    counter += 1
    z[counter] = t.values()

print(z)

a = 400
b = 400
print(id(a) == id(b))

print(hex(12345))


class test:
    t = 'asd'

    def s(self, t):
        print('AAAAAA')


test().s(t)

        # semantics_handler = test()
        # semantics_handler.abs_path()
