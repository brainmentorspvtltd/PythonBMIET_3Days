import matplotlib.pyplot as plt

ages = [23,45,18,47,89,78,67,66,87,34,45,28,25,19,22]

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages, bins, rwidth=0.8)
plt.show()
