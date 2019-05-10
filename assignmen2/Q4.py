#Author:Manish Puri
#Q4

def findcubes():
    lis = []
    for x in range(1,50):
        if x%2!=0:
            lis.append(x**3)
    return lis

print(findcubes())