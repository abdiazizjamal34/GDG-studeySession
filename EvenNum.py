

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num = []

for i in range(1, 21):
    num.append(i)

even_sum = 0

evenNum = []

for i in num:
    if i % 2 == 0:
        evenNum.append(i)
        

for i in evenNum:
   print(i)

 

