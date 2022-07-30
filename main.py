import math
import time

dairy = {'Milk': 2.3, 'Butter': 4.5, 'Eggs': 3.4, 'Cheese Slices': 3.15, 'Evaporated Milk Creamer': 1.4, 'Milo': 12.4,
         'Biscuits': 5.3, 'Yogurt': 0.95}
packagedgoods = {'Bread': 2.7, 'Cereal': 7, 'Crackers': 3.1, 'Chips': 2.6, 'Raisin': 2.1, 'Nuts': 2, 'Green Bean': 1.05,
                 'Barley': 1.05}
cannedgoods = {'Tomato': 1.45, 'Button Mushroom': 1.15, 'Baking Bean': 1.35, 'Tuna Fish': 1.45, 'Kernel Corn': 1.25,
               'Sardine Fish': 1.1, 'Chicken Luncheon Meat': 1.95, 'Pickled Lettuce': 0.95}
condiments_sauce = {'Fine Salt': 0.8, 'Sea Salt Flakes': 1.3, 'Chicken Stock': 3.15, 'Chilli Sauce': 2.65,
                    'Oyster Sauce': 4.5, 'Sweet Soy Sauce': 3.75, 'Tomato Ketchup': 3.2, 'Sesame Oil': 4.95}
drink_beverages = {'Green Tea Canned 330 ML': 15, 'Blackcurrant Ribena 330 ML': 31, '100 Plus 24 Cans': 15,
                   'Orange Cordial 2 Litre': 3.9, 'Mineral Water 24 x 600 ML': 7, 'Pineapple juice': 0.8,
                   'Nescafe Coffee': 9.9, 'Coke 24 Cans': 12.4}

dairyReadable = list(dairy.values())

all = [dairy, packagedgoods, cannedgoods, condiments_sauce, drink_beverages]

cart = {}
total = {}

print('--------------------')
print("1 - Dairy \n2 - Packaged Goods \n3 - Canned Goods \n4 - Condiments/Sauces \n5 - Drink & Beverages")
print('--------------------')
UserInput = input("Enter Category: ")
print('--------------------')

def dairyList():
    for key in dairy:
        rounded_dairy = '{:.2f}'.format(round(dairy[key], 2))
        print(key, " ", "$", rounded_dairy, sep='')
        print('--------------------')
def packagedgoodsList():
    for key in packagedgoods:
        rounded_packagedgoods = '{:.2f}'.format(round(packagedgoods[key], 2))
        print(key, " ", "$", rounded_packagedgoods, sep='')
        print('--------------------')

def cannedgoodsList():
    for key in cannedgoods:
        rounded_cannedgoods = '{:.2f}'.format(round(cannedgoods[key], 2))
        print(key, " ", "$", rounded_cannedgoods, sep='')
        print('--------------------')

def condiments_sauceList():
    for key in condiments_sauce:
        rounded_condiments_sauce = '{:.2f}'.format(round(condiments_sauce[key], 2))
        print(key, " ", "$", rounded_condiments_sauce, sep='')
        print('--------------------')

def drink_beveragesList():
    for key in drink_beverages:
        rounded_drink_beverages = '{:.2f}'.format(round(drink_beverages[key], 2))
        print(key, " ", "$", rounded_drink_beverages, sep='')
        print('--------------------')

def category():
    if UserInput == "1":
        dairyList()
    elif UserInput == "2":
        packagedgoodsList()
    elif UserInput == "3":
        cannedgoodsList()
    elif UserInput == "4":
        condiments_sauceList()
    elif UserInput == "5":
        drink_beveragesList()
    else:
        print('Not an Option')
        quit()

category()

def quantity(a):
    input2 = input("Quantity: ")
    try:
        input2 = int(input2)
    except:
        print("Enter a number!")
        quit()
    print("Calculating...")
    time.sleep(0.25)
    cart[input1] = input2
    if input1 in a:
        print("[CHECK] Item is in the dictionary.")
        time.sleep(0.25)
    else:
        print("[Error 001]")
    totalTemp = a[str(input1)] * input2
    if input1 in a:
        total[input1] = totalTemp
    else:
        print("[Error 002]")

while True:
    #print("--------------------")
    print("End - Check out and pay \nCart - Check your cart \nCategory - Change category of groceries")
    print("--------------------")
    input1 = input("Enter your choice: ")

    # cart = ['--------------------\n Start \n--------------------']

    if input1 == "End":
        print('--------------------')
        print("Ended.")
        quit()
    elif input1 == "Cart":
        print('--------------------\n Start \n--------------------')
        for x in cart:
            ()
        for y in total:
            print(y, " | $", total[y], " | x", cart[x], sep="")
        #for items in cart:
            #for i2 in total:
                #print(i2, ", $", total[i2], sep="")

            #print(items, cart[items])

        print('--------------------')
    elif input1 == "Category":
        print("1 - Dairy \n2 - Packaged Goods \n3 - Canned Goods \n4 - Condiments/Sauces \n5 - Drink & Beverages")
        print('--------------------')
        UserInput = input("Enter Category: ")
        print('--------------------')
        category()

    elif input1 in dairy:
        a = dairy
        b = input1
        quantity(a)
        print("Added Dairy product!")
        print('--------------------')

    elif input1 in packagedgoods:
        a = packagedgoods
        b = input1
        quantity(a)
        print("Added Packaged Goods product!")
        print('--------------------')
    elif input1 in cannedgoods:
        a = cannedgoods
        b = input1
        quantity(a)
        print("Added Canned Goods product!")
        print('--------------------')
    elif input1 in condiments_sauce:
        a = condiments_sauce
        b = input1
        quantity(a)
        print("Added Condiments Sauce product!")
        print('--------------------')
    elif input1 in drink_beverages:
        a = drink_beverages
        b = input1
        quantity(a)
        #cart.append(input1)
        print("Added Drink & Beverages product!")
        print('--------------------')
    else:
        print("Not an option.")
        print('--------------------')
