num = 123456789

total = 0

while num:
    digit = num % 10
    total += digit
    num //= 10

print(total)