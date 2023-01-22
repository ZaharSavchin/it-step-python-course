def generator():
    n = 1
    while True:
        yield n
        n += 2


g = generator()
for i in g:
    print(i)
