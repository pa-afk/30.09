# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:04:28 2025

@author: 6vsk.viesis1
"""
# 1. uzdevums
#s1 = [1, 2, 3, 4, 5]
#print(s1)
#print(s1[0])
#print(s1[4])

#user = int(input('Enter int:'))
#s1.append(user)
#print(s1)
#s1.remove(1)
# %%

#2. uzdevums
saraksts = []
for i in range(0, 5):
    x = int(input('x:'))
    saraksts.append(x)
    print(saraksts)
    
result = 0
for i in range(5):
    result += saraksts[i]
print(result)
    

# %%
    
