a, b, c = int(input()), int(input()), int(input())
if (a + b) % 2 != 0:
    print('YES')
elif (b + c) % 2 != 0:
    print('YES')
elif (a + c) % 2 != 0:
    print('YES')
else:
    print('NO')