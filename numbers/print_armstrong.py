print('Armstrong Number from 1 to 10000000')
for i in range(1, (9**3)*7):
    # (9**3)*7) range because Tong told about max outbound range.
    num = i

    total = 0

    while num:
        digit = num % 10
        total += digit ** 3
        num //= 10

    if total == i:
        print(i)
print('Successful.')