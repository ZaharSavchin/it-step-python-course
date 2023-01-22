def fib_generaror(n: int):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1, fib2 = fib2, fib_sum
        i += 1
        yield fib2


fib = fib_generaror(10)
# for num in fib:
#     print(num)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


