import random

user_name = input("Enter your name : ")
print("Welcome",user_name)

hello_intent = ['hi','hello','hey','hie','good morning']
bye_intent = ['bye','see you','bie','tc', 'ttyl']

print("How may I assist you ?")
while True:
    user_msg = input(">> ")
    user_msg = user_msg.lower()
    if user_msg in hello_intent:
        cpu_msg = random.choice(hello_intent)
        print(cpu_msg)
        #print("Hello")
    elif user_msg in bye_intent:
        cpu_msg = random.choice(bye_intent)
        print(cpu_msg)
        #print("Bye Take Care")
        break
    else:
        print("I don't understand")







