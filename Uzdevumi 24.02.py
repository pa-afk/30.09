#%%1
"""""
def greet(name):
    print(f'Sveika,{name}!')
greet("Anna")
"""""
#%%2
"""""
def sum_numbers(a, b):
    result = a + b
    return result
print(sum_numbers(5, 3))
"""""
#%%3
"""""
def is_even(n):
    i = 2
    n = int(input("Enter:"))
    if n % i == 0:
        return("True:")
    else:
        return("False:")
print(is_even(77))
"""""
"""""
def factorial(n):
    result = 1 
    for i in range(1, n +1):
        result *= i
    return result
print(factorial(5))
"""""


def fizzbuzz(n):
    if n % 3 ==0 and n % 5 == 0:
        print("FizzBuzz")
    if n % 3 == 0:
        print("Fizz")
    if n %5 == 0:
        print("Buzz")
    
print(fizzbuzz(33))
    
    
    
   
    