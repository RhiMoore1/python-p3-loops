#!/usr/bin/env python3



def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
        
        

# def square_integers(int_list):
#     squared_list = []
#     for num in int_list:
#         squared_list.append(num ** 2)
#     return squared_list

def square_integers(int_list):
    squared_integer_list = [num**2 for num in int_list]
    return squared_integer_list

result = square_integers([1, 2, 3, 4])
print(result)

    
# def fizzbuzz():
#     for i in range(1, 101):
#         if not i % 5 and not i % 3:
#             print("FizzBuzz")
#         elif not i % 5:
#             print("Buzz")
#         elif not i % 3:
#             print("Fizz")
#         else:
#             print(i)



def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

# result = fizzbuzz(101)
# print(fizzbuzz)
