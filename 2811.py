# %%
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 25 12:08:51 2024

@author: 6vsk.viesis1
"""

# %%
       
augstums = 5
x = 1

for i in range(0, augstums):
    print(' '*(augstums - i), end="")
    print('*'*x,end='')
    print()
    x = x + 2


