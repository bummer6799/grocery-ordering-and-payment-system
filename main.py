import math


Dairy = ["Milk", "Butter", "Eggs", "Cheese slices", "Evaporated Milk Creamer", "Milo", "Biscuits", "Yogurt"]
# DairyPrices = ["2.30", "4.50", "3.40", "3.15", "1.40", "12.50", "5.30", "0.95"]
DairyPrices = [2.30, 4.50, 3.40, 3.15, 1.40, 12.50, 5.30, 0.95]
DairyPricesGST = [i * 107/100 for i in DairyPrices]
for i in DairyPricesGST:
    print("%.2f" % DairyPricesGST)
print(*Dairy + DairyPricesGST, sep='\n')



UserInput = int(input("Selection:"))
print(Dairy[UserInput], DairyPricesGST[UserInput])
