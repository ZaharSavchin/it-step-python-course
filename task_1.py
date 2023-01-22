class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start % 2 == 1:
            self.start += 1
            return self.start
        elif self.start >= self.end - 1:
            raise StopIteration("Out of numbers!")
        self.start += 2
        return self.start

    def __iter__(self):
        return self


al = EvenRange(3, 11)
# for i in al:
#     print(i, end=" ")
print(next(al))
print(next(al))
print(next(al))
print(next(al))
print(next(al))




