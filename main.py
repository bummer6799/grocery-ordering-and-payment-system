import math


dairy = {'Milk':2.3, 'Butter':4.5, 'Eggs':3.4, 'Cheese Slices':3.15, 'Evaporated Milk Creamer':1.4, 'Milo':12.4, 'Biscuits':5.3, 'Yogurt':0.95}

UserInput = input("1 - Dairy \nEnter Category: ")

if UserInput == "1":
    for key in dairy:
        print(key,dairy[key])