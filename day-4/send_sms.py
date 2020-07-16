from twilio.rest import Client
# importing the requests library 
import requests 
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC5e80d147908cda7e59bc0d336c04c00d'
auth_token = 'e8fdf8b59e17753967bfd1dcd9cb6d02'
client = Client(account_sid, auth_token)



message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12513697336',
         to='+14255338314'
     )

# API endpoint
URL = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=8c041850bfb64656b32ec72ba28edcc6"
# Defining the parameters
PARAMS = {"ingredients": "butter,flour,milk", "number": 3, "limitLicense": True, "ranking": 1, "ignorePantry": True} 
# Sending GET request and saving the data
r = requests.get(url = URL, params = PARAMS) 
# Extracting data in JSON format 
data = r.json() 
# print(data)
recipes = {}
for recipe in data:
    usedIngredients = []
    missedIngredients = []
    allIngredients = []
    for used in recipe["usedIngredients"]:
        usedIngredients.append(used["original"])
    for missed in recipe["missedIngredients"]:
        missedIngredients.append(missed["original"])
    allIngredients.append(usedIngredients)
    allIngredients.append(missedIngredients)
    recipes[recipe["title"]] = allIngredients


for dish, ingredients in recipes.items():
    print(f"{dish}: ")
    print(f"Ingredients you already have: {ingredients[0]} \nIngredients you need: {ingredients[1]}")



print(message.sid)