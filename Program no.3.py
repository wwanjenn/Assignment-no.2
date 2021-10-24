#Input Functions
totalCash = int(input("How much money do you have?: "))
priceApple = int(input("How much is an Apple?: "))

#Formula for the Program
amountApple = totalCash // priceApple
changeCash = totalCash % priceApple

#Output Function
print(f'You can buy {amountApple} apples and your change is {changeCash} pesos.')