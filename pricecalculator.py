import time

itemsDict = {'A':1.5, 'B':2, 'C':3}
itemsReadable = list(itemsDict.values())
total = {}
for i in itemsDict:
    print(i, "=", itemsDict[i])
input1 = input("input1 : Enter your Item: ")
input2 = input("input2 : How many: ")

try:
    input2 = int(input2)
except:
    print("Enter a number!")
    quit()
print("Calculating...")
time.sleep(1)
if input1 in itemsDict:
    print("[CHECK] Item is in the dictionary.")
else:
    print("[Error 001]")
totalTemp = itemsDict[str(input1)]*input2
print("Total cost of your selection: ", totalTemp)

if input1 in itemsDict:
    total[input1] = totalTemp
    for i2 in total:
        print(i2,", $", total[i2], sep="")
else:
    print("[Error 002]")