# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:01:14 2024

@author: 6vsk.viesis1
"""

#import random
#random.seed(6)

#for i in range(4):
 #print(random.random())
# %%
#a = random.random()
#b = random.randint(0,10)
#c = random.choice([11,15,16,17]) 
#print(a, b, c)
# %%

#dice = random.randint(1,6)
#print(dice)
# %%
import random
lielaka_summa = 0

for i in range(10):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'{dice1} | {dice2}')
    if dice1 > dice2:
      print(f'{dice1} {dice2} | {dice1} | {dice1 + dice2}')
    elif dice2 > dice1:
         print(f'{dice1} {dice2} | {dice2} | {dice1 + dice2}')
         
    else:
     pass 
    if dice1+dice2 > lielaka_summa:
         lielaka_summa = dice1+dice2 
         
         print(lielaka_summa)
# %%
    x= int(input("Enter skaitlis:"))
    y = random.choice([1,2,3,4,5,6,7,8,9,10])
    print(random.choice([1,2,3,4,5,6,7,8,9,10]))
    if x == y:
        print("Uzminets")
    elif x>y:
        print("Mazaks")
    elif x<y:
        print("Lielaks")
