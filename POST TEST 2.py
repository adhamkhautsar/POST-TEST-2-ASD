import os
from copy import deepcopy
os.system("cls")

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

print(var)

data1 = var[0]
print(f"\n\nIndex 0 = {data1}")
print("="*23)

data2 = var[1]
print(f"\n\nIndex 1 = {data2}")
print("="*23)

data3 = var[2]
print(f"\n\nIndex 2 = {data3}")
print("="*23)

data4 = var[3][0]
print(f"\n\nIndex 3 Kolom 0 = {data4}")
print("="*23)

data5 = var[3][1]
print(f"\n\nIndex 3 Kolom 1 = {data5}")
print("="*23)