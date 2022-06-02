#!/usr/bin/python3
# Have user enter their investment amount
money = input('How much to invest: ')
# Have user enter expected interest rate
rate = input('Interest Rate: ')
# convert to float
money = float(money)
# convert interest rate to float and round percentage rate by 2 digits 
rate = float(rate) * .01
# Each year, investment will increase by investment+investment*interest rate
for i in range(10):
    money = money + (money * rate)
# print out earnings after 10 years period
print("Your cashout after 10 years is: {:.2f}".format(money))
