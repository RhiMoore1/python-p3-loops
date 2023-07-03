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


    
def fizzbuzz():
    for i in range(1, 101):
        if not i % 5 and not i % 3:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

