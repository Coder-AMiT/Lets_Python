a = [1,2,3,'hi',5,'python','3.6',True,False]

int_count = 0
str_count = 0

for item in a:
    if type(item) == int:
        int_count += 1
    if type(item) == str:
        str_count += 1

print('int count :: ', int_count)
print('str count :: ', str_count)