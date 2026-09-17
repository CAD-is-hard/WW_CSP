# WW, Your Budget

income = float(input("What is your monthly income: "))

housing = float(input("What is your rent or mortgage: "))

utilities = float(input("What is your monthly utilities cost: "))

groceries = float(input("What is your monthly grocery cost: "))

transportation = float(input("What is your transportation cost: "))

housingpercent = ((housing/income)*100)

utilitypercent = (round((utilities/income)*100,0))

grocerypercent = (round((groceries/income)*100,0))

transportationpercent = (round((transportation/income)*100,0))

savings = (round(income/10,0))

spending = (round(income-(housing+utilities+groceries+transportation+savings),2))

print(f"Your housing cost is ${housing} and that is {housingpercent}% of your income.")

print(f"Your utilities cost is ${utilities} and that is {utilitypercent}% of your income.")

print(f"Your groceries cost is ${groceries} and that is {grocerypercent}% of your income.")

print(f"Your  cost is ${transportation} and that is {transportationpercent}% of your income.")

print(f"You should save ${savings} a month, that is 10% of your income.")

print(f"You have ${spending} of spending money each month.")