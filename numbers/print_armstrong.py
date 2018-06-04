print('Armstrong Number from 1 to 10000000')
for i in range(1, 10000000):
    num = i

    total = 0

    while num:
        digit = num % 10
        total += digit ** 3
        num //= 10

    if total == i:
        print(i)
print('Successful.')