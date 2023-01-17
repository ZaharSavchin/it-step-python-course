def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    print(x, a, y)


def bar(a):
    try:
        foo(a)
    except ZeroDivisionError as err:
        print(f"your error: {err}")


def bzz(a):
    try:
        bar(a)
    except IndexError as err_1:
        print(f"your error: {err_1}")

bzz(0)
bzz(4)
bzz(2)