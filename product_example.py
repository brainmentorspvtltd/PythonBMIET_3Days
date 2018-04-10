products = [
    {"id":101,'name':'Apple','price':90000,'color':'white'},
    {"id":102,'name':'Samsung','price':45000,'color':'white'},
    {"id":103,'name':'Vivo','price':25000,'color':'silver'},
    {"id":104,'name':'Oppo','price':30000,'color':'gray'},
    {"id":105,'name':'Apple','price':50000,'color':'silver'},
    {"id":106,'name':'Apple','price':55000,'color':'black'},
    {"id":107,'name':'Vivo','price':18000,'color':'black'},
    {"id":108,'name':'Redmi','price':15000,'color':'white'},
    {"id":109,'name':'Redmi','price':12000,'color':'silver'},
    {"id":110,'name':'Samsung','price':35000,'color':'gray'},
    ]

search_data = input("Enter product to search : ")

##for data in products:
##    if data['name'] == search_data:
##        print(data)

##def func_1(data):
##    return data['name'] == search_data
##
##list(filter(func_1, products))

# Alternative using lambda
d = list(filter(lambda data : data['name'] == search_data, products))

for i in d:
    print(i)












