#Author:Manish Puri
#Q7

def findinttype(x):
    for el in x:
        if not isinstance(el, int):
            return False
    return True
            
print(findinttype([1,2,3,4.5]))
