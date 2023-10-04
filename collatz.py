c0 = int(input("Enter a non-negative or non-zero integer number: "))
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    elif c0 % 2:
        c0 = 3 * c0 + 1
    elif c0 != 1:
        c0 = 2
    print(c0)
    steps += 1

print("Steps =", steps)
