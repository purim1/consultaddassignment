#Author:Manish Puri
#Q3

import re
def returnfreq(st):
    dis = {}
    for el in st:
        if re.findall("[^a-zA-Z0-9]+", el):
            if el in dis.keys():
                dis[el]+=1
            else:
                dis[el]=1
    return dis

st = "aaabbbc&&*c"
print(returnfreq(st))
