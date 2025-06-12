age=int(input("Please enter your age: "))

if age<13:
    print("You are a child")
elif age>=13 and age<18:
    print("You are a teenager")
elif age>=18 and age<65:
    print("You are an adult")
elif age>=65:
    print("You are an elder")
else:
    print ("Wrong number.")