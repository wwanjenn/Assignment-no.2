totalCash = int(input("How much money do you have?: "))
priceApple = int(input("How much is an Apple?: "))

amountApple = totalCash // priceApple
changeCash = totalCash % priceApple

print(f'You can buy {amountApple} apples and your change is {changeCash} pesos.')