#Author:Manish Puri
#Q2

x = [1,2,3,4,5,6,7,8,9,10]

def pairnos(x):
    lis=[]
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j and (x[i]+x[j])%2==0 and (x[i]+x[j]) in range(1,21):
                lis.append(tuple((x[i],x[j])))


    return(lis)

print(pairnos(x))   