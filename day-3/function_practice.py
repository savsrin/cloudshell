#Function 1
def costOfDisneyFor(number_of_adults, number_of_children, number_of_days):
    adult_cost = number_of_adults * 100
    print("Calculated adult cost at " + str(adult_cost)) 
    child_cost = number_of_children * 90
    print("Calculated child cost at " + str(child_cost)) 
    daily_cost = adult_cost + child_cost
    total_cost = daily_cost * number_of_days
    return total_cost
#Function1 Q's: 
#How many parameters did we use to define this function? 3
#What datatype will we use as arguments when we call the function? ints
#What datatype will the return value be? float
#Right now, if we ran this program, nothing would actually happen. Why is that? no print
################################################################################
#Function 2
def greetPlayer(name = "User"):
  print("Welcome to the game, " + name + ".")
  print("Your current level is 1.")
greetPlayer("David") # Code if the user provides their name
greetPlayer()
#function 2 Q's 
#What is the default argument? User
#Which greeting will USE the default argument? greetPlayer()
################################################################################
#Function 3
def createUser(name, email, password = "abcd1234"):
  # Some code to create the user
createUser("John Smith", "Jsmith123@gmail.com")
createUser("Marta Guzman", "MartaG789@gmail.com", "Puppies1")
createUser("Artie Krausmann")
#How many arguments does this function take? 2 required, 1 optional
#How many of those arguments are required? How many are optional? 
#What will John Smith's password be? abcd1234
#Which line will throw an error? Why? third one, not all parameters