#Author: Manish Puri

user_in = input("Enter a number: ")

if user_in < 100:
   print "Value is less than 100"
   if user_in == 50:
      print "Value is 150"
   elif user_in == 100:
      print "Value is 100"
   elif user_in == 50:
      print "Which is 50"
   elif user_in < 20:
      print "Value is less than 20"
      
elif user_in >= 100 and user_in <=1000:
    print "Value equals or greater than 100 but less than 1000"

else:
   print "Value is larger than 1000"
