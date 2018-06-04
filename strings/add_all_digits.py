a = '123 and 45 are numbers,also 67 even 89 with special char &^***'

total = 0

for letter in a:
    if letter.isdigit():
        total += int(letter)

print(total)