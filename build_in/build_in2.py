import itertools

def test_count():
    natuals = itertools.count(1)
    for n in  natuals:
        print n
    pass

def test_circle():
    # cs = itertools.cycle("abc")
    # i = 0
    # for c in cs:
    #     if (i < 10):
    #         print c
    #         i = i +1
    #     else:
    #         break

    cs = itertools.count(1)
    nx = itertools.takewhile(lambda x: x < 100, cs)
    for n1 in nx:
        print n1
    pass



# # test_count()
test_circle()


