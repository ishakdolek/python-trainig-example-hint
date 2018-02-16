
import requests

first_exchange="TRY"
second_exhange="USD"
url = "https://api.fixer.io/latest?base="


response=requests.get(url+second_exhange)

json_format=response.json()

test=json_format["rates"][first_exchange]

# inut_valeu=int(input("Değer:"))

print(test*100)
