# find all the index of 2

a = [1,2,2,4,5,6,2,2,3,2]

# 1st way
for index, item in enumerate(a):
    if item == 2:
        print(index)


# 2nd way

index = 0
while index < len(a) and 2 in a[index:]:
    index = a.index(2,index)
    print(index)
    index += 1
