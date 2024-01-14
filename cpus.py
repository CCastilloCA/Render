product_price = 12.0
product_qty = 5

def total_price():
    product_price = 11.0
    product_qty = 4
    print(f'Precio total:{product_price*product_qty}')

total_price()

product_price = 12.0
product_qty = 5 

def total_price():
    print(f'Precio total: {product_price*product_qty}')

total_price()

def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, 5.1, 'A', 'B')


def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(dist_miles=409, loc_from='A', loc_to='B', mpg=35, price=5.1)

# list_of_words.py
def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

list_of_words("María tenía un pequeño cordero", sep="a")
print("Hola de parte de list_of_words.py")


def greetings(name: int) -> str:
    return f"Hola {name}!"

print(greetings(10)) 

mage = {'health': 50, 'damage': 10, 'knowledge': 95}
knight = {'health': 100, 'damage': 25, 'knowledge': 20}

arthur = knight.copy() # hacer una copia del diccionario 'knight' original
arthur['name'] = 'Arthur' # reemplazar el nombre dentro de la copia

richard = knight.copy() # hacer otra copia del diccionario 'knight' original
richard['name'] = 'Richard' # reemplazar el nombre dentro de la copia

def heal(character): # crear la función que cambia la salud
    character['health'] += 20

heal(richard) # llamar a la función para cambiar la salud de Richard 

class Knight: # crear la clase Knight
    def __init__(self, name):
        # establecer parámetros
        self.health = 100
        self.damage = 25
        self.knowledge = 20
        self.name = name
    def heal(self, amount):
        self.health += amount
    def learn(self, amount):
        self.knowledge += amount

arthur = Knight('Arthur')

arthur.heal(10)
arthur.learn(2)

print(arthur.health)
print(arthur.knowledge)

import json
import requests # librería para obtener datos de internet

# descargar (obtener) un archivo json de internet
data = requests.get('https://dummyjson.com/products/1')

# extraer el contenido del archivo json descargado
text = data.text

# análisis sintáctico del contenido mediante la función loads
print(json.loads(text)) 

import requests

response = requests.get("https://api.frankfurter.app/latest")
print(response)

import requests

response = requests.get("https://api.frankfurter.app/latest")
print(response.json())


import requests

params = {"from":"USD", "to":"GBP", "amount":20}
res = requests.get("https://api.frankfurter.app/latest", params=params)
print(res.json()) 

import requests

response = requests.get("https://api.frankfurter.app/latest")

print(response.headers['Server'])
print(response.headers['Content-Type'])


