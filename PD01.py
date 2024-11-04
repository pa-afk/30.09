# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:13:24 2024

@author: 6vsk.viesis1
"""

x= str(input("Enter x:"))
y= int(input("Enter y:"))
print(float(x))
print(str(y))
# %%   2

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print (a+b)
print (a-b)
print (a*b)
print (a/b)

# %%  3

x= int(input("Enter x:"))
if x > 0:
    print("x ir pozitivs")
elif x < 0:
    print("x ir negativs")
else:
    print("x ir nulle")
    
# %%  4
    
x= int(input("Enter x:"))
y= int(input("Enter y:"))
result1= 4*x**(y+3) + 15+y
result2=(5*y**x-144*x+2)/((x+y)**2)
result3= (2 + x - 2*x*y)/((y)/(x+y))
print(result1)
print(result2)
print(result3)
# %%  5

x=int(input("Enter atzimi:"))
if x == 9 or x == 10:
     print("A")
elif x == 8 or x == 7:
    print("B")
elif x == 6 or x == 5:
    print("C")
elif x == 4 or x == 3:
    print("D")
elif x == 2 or x == 1:
    print("E")
elif x == 0:
    print("F")
else:
    print("kluda")
    
    