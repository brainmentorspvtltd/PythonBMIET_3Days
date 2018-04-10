def temp_conv(cel):
    return 9 / 5 * cel + 32

temp = [33.5,32.1,37.2,33.9,29.1]

#for t in temp:
#    print(temp_conv(t))

f = list(map(temp_conv, temp))
print(f)
