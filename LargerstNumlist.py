
import random

num = []
# generate a randem list of 10 numbers
for i in range(10):
    num.append(random.randint(1, 100))

print(num)

largest = num[0]

for i in num:
    if i > largest:
        largest = i

print("The largest number in the list is: ", largest)