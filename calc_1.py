def add(x,y):
    result = x + y
    print("Result is",result)
def sub(x,y):
    result = x - y
    print("Result is",result)
def div(x,y):
    result = x / y
    print("Result is",result)
def mul(x,y):
    result = x * y
    print("Result is",result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

user_ch = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))


##todo = {
##    "1" : add(num_1,num_2),
##    "2" : sub(num_1,num_2),
##    "3" : div(num_1,num_2),
##    "4" : mul(num_1,num_2)
##    }

todo = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
    }

todo.get(user_ch)(num_1,num_2)

##user_ch = 1
##
##todo.get(1)()
##add()


    
