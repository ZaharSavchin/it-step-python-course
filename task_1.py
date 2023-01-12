from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

n1 = Number(10)
n2 = Number(10)
n3 = Number(20)

print(n1 == n2)
print(n1 < n3)
print(n3 > n2)
print(n1 == n3)
print(n1 != n2)
print(n1 >= n2)
print(n1 <= n2)