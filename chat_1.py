user_name = input("Enter your name : ")
print("Welcome",user_name)

print("How may I assist you ?")
while True:
    user_msg = input(">> ")
    user_msg = user_msg.lower()
    if user_msg == "hi" or user_msg == "hello":
        print("Hello")
    elif user_msg == "bye" or user_msg == "Bye":
        print("Bye Take Care")
        break
    else:
        print("I don't understand")







