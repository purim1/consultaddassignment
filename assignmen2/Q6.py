#Author:Manish Puri
#Q6

def leneachword(x):
    x = x.split()
    for el in x:
        print ("Length of ", el, " is ", len(el))


print(leneachword("I am a happy guy"))

