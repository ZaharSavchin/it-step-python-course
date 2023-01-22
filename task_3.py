def show_letters(some_str: str):
    for i in some_str:
        if i.isalpha():
            yield i


s = show_letters('my, age, is: 26!')
for i in s:
    print(i, end="")
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
