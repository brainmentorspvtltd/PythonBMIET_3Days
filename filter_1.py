def evn_num(num):
    return num % 2 == 0

numbers = []

for i in range(101):
    numbers.append(i)

#for n in numbers:
#    print(evn_num(n))

e_num = list(filter(evn_num, numbers))
print(e_num)






