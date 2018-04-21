
from numbers import Numbers

for w in range(1,10):
    n = Numbers(w,1234567890)
    numbers = n.getAllNumbers()
    print('\n')
    for x in numbers:
        print("")
        for y in x:
            print(y, end=" ")

