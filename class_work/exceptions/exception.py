def add(a: float, b: float) -> float | None:
    try:
        #    c = a + 'b'
        #     return a / b
        # except TypeError:
        # lst = [1, 2, 3]
        # print(lst[6])
        # file = open('file.txt', mode='r', encoding='utf - 8')
        # print(file.read())
        # print('About to close')
        # file.close()
        print(a / b)
    except ZeroDivisionError:
        print("Cant divide with zero")
        return None
    except (TypeError, NameError):
        print("Type Error")
    except IndexError:
        print("Index out off bound")
    except FileNotFoundError:
        print("file not found")
    else:
        print("Owo epo ")
    finally:
        print("About to close")


print(add(1, 2))
