#!/usr/bin/env python3



def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
        
        

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list




def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num