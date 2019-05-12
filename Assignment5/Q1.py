
# Author: Manish Puri
# Consultadd Assignment 5

import string
import random
import functools as ft

# Q1

#res = ["TRUE" if i%2!=0 else "FALSE" for i in range(1,3000)]
res = [i % 2 == 0 for i in range(1, 3000)]
print(res)


# Q2

def multiply(x, y):
    return x*y


print(ft.reduce(multiply, range(1, 10)))


# Q3

def game(functiondemo):
    def gamefunction():
        print("here is the message")
        functiondemo()
        print("end of message")
    return gamefunction


def helpme():
    print("Please help me")


final_message = game(helpme)
final_message()


# Q4

def printmaxel(x):
    with open(x, "r") as f:
        arr = []
        for line in f:
            arr.append(line)

        maxel = ""
        maxl = 0
        for el in arr:
            if len(el) > maxl:
                maxl=len(el)
                maxel = el
        return maxel


print(printmaxel("ans.txt"))


# Q5
class Triangle():
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def area(self):
        return 0.5*self.b*self.h


triangle = Triangle(3, 4, 5)
print(triangle.area())


# Q6
def passwordGenerator(N=10):
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(password, k=N))


print(passwordGenerator(7))
print(passwordGenerator(30))


# Q7
def newList(arr):
    return [arr[0], arr[-1]]


print(newList([1, 2, 3, 4]))


# Q8
def createThird(list1, list2):
    return [list1[x] for x in range(0, len(list1), 2)] + [list2[x] for x in range(1, len(list2), 2)]


a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e', 'f']
print(createThird(a, b))


# Q9
def sliceList(arr, size=3):
    temp = [arr[i:i+size] for i in range(0, len(arr), size)]
    temp2 = [x for x in temp if len(x) == size]
    return temp2


print(sliceList([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# Q10
def checkList(arr, dis):
    temp = [x for x in arr if x in dis.values()]
    return temp


a = [1, 2, 3, 4, 5]
dis = {'a': 10, 'b': 2, 'c': 40, 'd': 50}
print(checkList(a, dis))
