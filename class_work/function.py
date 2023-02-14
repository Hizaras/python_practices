# # name = "Hadiza"
# # print(globals())
# #
# #
# # def func(num):
# #     print(locals())
#
#
# a = 5
#
#
# def func1():
#     global a
#     a += 7
#     print(a)
#
# # func()




a = 5
def func1():
    b += 2
    print(b)

    def inner_func():
        nonlocal b
        b += 2
        print(b)
    inner_func()
    print()