#!/usr/bin/python

import json

needed = open('needed.json', 'r')
available = open('available.json', 'r')

neededList = json.load(needed)
availableList = json.load(available)

print("Antal armband som skall göras: ", end="")
count = int(input())

print("Pärlor som behövs:")
for key in neededList :
    neededList[key] *= count
    neededList[key] -= availableList[key]
    if(neededList[key] > 0):
        print(f"{key}:\t{neededList[key]}")

with open('result.json', 'w') as resultFile:
    json.dump(neededList, resultFile, indent=2, ensure_ascii=False)