import sys
import time


def gera():
    var = 1
    yield var
    var = 2
    yield var
    var = 3
    yield var


g = gera()

print(g)
print(hasattr(g, "__iter__"))

for v in g:
    print(v)


l1 = [x for x in range(100000)]
print(type(l1))
l2 = (x for x in range(100000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
for v in l2:
    print(v)

print(sys.getsizeof(l2))
