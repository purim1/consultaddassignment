# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:25:14 

@author: MANISH
"""

import pickle

class BankingOperations:

    def addNewAccount(self):
        self._fname=input("Enter first name ")
        self._lname=input("Enter last name ")
        self._age = input("Enter age " )
        self._address = input("Enter address ")
        self._contact = input("Enter contact number ")
        self._gender = input("Enter gender ")
        self._accounttype= input("checking or savings ")
        self._accountbeneficiary = input("account has beneficiary? ")
        self._SSN = input("Enter last 4 of Social Security Number ")
        self._accountnumber= int(self._SSN) + ord(self._accounttype[0])
        self._accountBalance = input("Enter amount you would like to deposit now ")


    def printAccountDetails(self):
        print("First name is", self._fname)
        print("Last name is", self._lname)
        print("Age is", self._age)
        print("Address is", self._address)
        print("Contact is", self._contact)
        print("Gender is", self._gender)
        print("accounttype is", self._accounttype)
        print("beneficiary is", self._accountbeneficiary)
        print("SSN is", self._SSN)
        print("accoutn no", self._accountnumber)
        print("account balance", self._accountBalance)        


    def getaccountNumber(self):
        return self._accountnumber

    def getaccountBalance(self):
        return self._accountBalance

    
    def addAccountBalance(self,amt):
        bal = int(self._accountBalance) + int(amt)
        self._accountBalance=bal
    




count=0
accounts =[]
PIK = "pickle.dat"


def writetoCSV(com):
    with open(PIK, "wb") as f:     
        pickle.dump(com,f,pickle.HIGHEST_PROTOCOL)



def writetoCSVover(com):
    with open(PIK, "wb") as f:       
        pickle.dump(com,f,pickle.HIGHEST_PROTOCOL)



def readfromcsv():
    with open(PIK, "rb") as f:
        arr = pickle.load(f)
    return arr



while True:
    if count==3:
        print("You have exceeded maximum number of tries")
        break


    otp = int(input(("Welcome to the bank. Please enter 4 digit OTP number: ")))
    if otp != 1234:
        print("Sorry. Please enter valid OTP")
        count+=1
        continue


    print("1. Press 1 to add new account")
    print("2. press 2 to withdraw")
    print("3. press 3 to deposit")
    print("4. press 4 for balance inquiry")
    print("5. Pess 5 for demand draft")
    print("6. press 6 to cancel")
    
    option = int(input("What would you like to do toay? "))
    
    

    if option==1:
        
        accounts = readfromcsv()
        print("account details: ")

        useraccount = BankingOperations()
        useraccount.addNewAccount()

        accountno = int(useraccount.getaccountNumber())
        accounts.append(useraccount)

        writetoCSV(accounts)
        print("Successfully added account")

        
        accounts = readfromcsv()
        print("account details: ")
        
        for i in range(len(accounts)):
            if accounts[i].getaccountNumber() == accountno:
                accounts[i].printAccountDetails()                    



    elif option==2:
        useraccountnumber = int(input("Enter Account number to withdraw from: "))        

        accounts = readfromcsv()
        index=-1
        for i in range(len(accounts)):
            if accounts[i].getaccountNumber() == useraccountnumber:
                while True:
                    withdrawAmt = int(input("Enter amount to withdraw: "))
                    if withdrawAmt not in range(100,10000):
                        print("Limit exceeded. Please enter amount greater than 100 and less than 10000")
                        continue
                    else:
                        break

                index=i
                accounts[i].addAccountBalance(-withdrawAmt)
                print("Withdrawal successful")
                break
        
        writetoCSV(accounts)
        if index == -1:
            print("Account number not found")
                


    elif option==3:
        useraccountnumber = int(input("Enter Account number to deposit to: "))
        accounts = readfromcsv()
        index=-1

        for i in range(len(accounts)):
            if accounts[i].getaccountNumber() == useraccountnumber:

                while True:
                    addAmt = int(input("Enter amount to deposit: "))
                    if addAmt %5 !=0:
                        print("Error. Please enter deposit amount in multiples of 5")
                        continue
                    else:
                        break

                index=i
                accounts[i].addAccountBalance(addAmt)
                print("Deposit successful")
                break

        writetoCSV(accounts)
        if index == -1:
            print("Account number not found")
 


    elif option==4:
        useraccountnumber = int(input("Enter Account number for balance inquiry: "))
        accounts = readfromcsv()
        index=-1
        for i in range(len(accounts)):
            if accounts[i].getaccountNumber() == useraccountnumber:
                index = i
                print("account number is", accounts[i].getaccountNumber())
                print("account balance is", accounts[i].getaccountBalance())
    
        if index == -1:
            print("Account number not found")        
            


    elif option==5:
    
        fromaccountnumber = int(input("Enter account number from which demand draft is to be made: "))
        draftamt = int(input("Enter demand draft amount: "))
        toaccountnumber = int(input("Enter account number to which demand draft is to be made: "))

        accounts = readfromcsv()
        index1 = -1
        index2 = -1
        
        for i in range(len(accounts)):
            if accounts[i].getaccountNumber()==fromaccountnumber:
                print("from account found")
                index1=i
                break

        for j in range(len(accounts)):
            if accounts[j].getaccountNumber()==toaccountnumber:
                print("to account found")
                index2=j
                break

        if index1==-1 or index2 == -1:
            print("Please input valid account numbers")
        else:
            accounts[index1].addAccountBalance(-draftamt)
            accounts[index2].addAccountBalance(draftamt)
        writetoCSV(accounts)
        print("Demand draft completed")
        


    elif option==6:
        accounts = readfromcsv()
        print("hava a nice day")
        break
    
    
    else:
        print("Please enter valid operation")
        count+=1
