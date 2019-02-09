# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 01:56:50 2019

"""



def to_romanNumeral(number):
    numberToRomanNumeral = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
    #List that will be used to keep the Roman numeral to return
    returnList = []
    
    # loop through the list
    for (numeral, value) in numberToRomanNumeral:

        #while input number is not zero loop to subtract
        while value <= number:
            
            #subtract the value from the input number
            number -= value 
            returnList.append(numeral)

    return (''.join(returnList))


while True:
    inputnumber = input("Enter number: ")
    inputnumber= int(inputnumber)
    
    # check to see if the user input valid number
    while (inputnumber<=0):
        inputnumber = input("Please enter number higher than 0: ")
        inputnumber=int(inputnumber)
        
    print ("Roman Numeral: ", str(to_romanNumeral(inputnumber)))
