#Author: Manish Puri


user_in = input("Enter a number")
user_in = int(user_in)   
r = range(10,50)
if user_in in r:
    print("Yes I am in the range")
else:
    print("Oops")
