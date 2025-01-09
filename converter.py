import requests, json
from config import URL

stop = 0
currencies = requests.get(URL)
list_currency = currencies.json()

data = json.dumps(list_currency, indent=4)


print("Welcome! This system helps you to convert your money.")
available = int(input("To check available currencies enter 0, otherwise, enter 2: "))

if available == 0:
    print(data)



try:
    while stop != 1:
        money = float(input("Enter amount: "))
        if money == 1:
            break
        currency = input("Enter code of your currency: ")
        convert_currency = input("To which currency: ")

        result = ""
        for i in list_currency:
    
            if currency.upper() == i['code']:
                money_to_convert = float(i['cb_price']) 
                average = money * money_to_convert
        
                for l in list_currency:
                    if convert_currency.upper() == l['code']:
                        converted_currency = float(l['cb_price'])
                        result = average / converted_currency
            
            
        final = float(result)   
        print(f"Result: {money} {currency.upper()} = {final:.2f} {convert_currency.upper()}",)
        print()
        print("Remember: To stop program, enter 1!")
except ValueError:
    print('This currency is not availab!! Restart the project again and try available currencies')

print("Thank you to use our program. We are happy to see you again")
