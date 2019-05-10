# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:04:15 2019

@author: MANISH
"""
import random


pick,count = random.randint(1,20), 0
fname,lname = input("Enter firstname followed by lastname: ").split()
while True:
    if count==3: print("SORRY PROGRAM CRASHED") ; break
    try: userint = int(input("Enter no between 1 and 20: "))
    except: print("enter valid integer "); count+=1; continue   
    message = "OTP SUCCESSFULLY MATCHED!" if userint ==pick else "wrong input try again" if userint>20 else "ERROR!!! ENTER THE OTP AGAIN"
    if userint == pick: print(message); break
    print(message); count+=1    
    tryagain = input("Do you want to continue?" + " You have " +str(3-count) + " tries remaining. Please type Yes to continue or No to quit: ")
    if tryagain.lower() == "yes": continue
    else: break ; print("thanks for attempt!")