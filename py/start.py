# print("hello this is pyhton learning")
# # Exercise 1 calculate the area of a rectangle
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))

# area = length * width 
# print(f"The area is: {area}cm^2")

# # Exercise 2 mini shooping app
# item = input("What item do you want: ")
# price = float(input("What item do you want: "))
# quantity = int(input("What item do you want: "))

# total = price * quantity

# print(f"Your have bought {quantity} x {item}/s")
# print(f"The Total cost {total}FCFA")

# # Exercise three Madlibs games
# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing, animal): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")

# print(f"Today i went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}")

# If statement : do some code only when the condition is true and Else do something else
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Yor are eligible for a card")
# elif age < 0:
#     print("You are not human")    
# else:
#     print(f"You are {age} and the required age is 18 year.")


# Python Calculator
# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result, 2))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 2))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 2))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 2))
# else:
#     print(f"The {operator} is not valide") 
    
# # Python wieight converter
# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (k or l): ") 

# if unit == "k":
#     weight = weight * 2.205
#     unit = "Lbs."
# elif unit == "l":
#     weight = weight / 2.205
#     unit = "Kgs"
# else:
#     print(f"{unit} was not valid")
    
# print(f"Your weight is: {round(weight, 2)} {unit}")    

# # temperature convention in python
# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}F")
# elif unit == "F":
#     temp = round((temp - 32 ) * 5 / 9, 1)
#     print(f"The temperature in Celsuis is:  {temp} C")
# else:
#     print(f"{unit} is an invalid unit of mearsurement")   


# # conditional expression (ternary operation)
# num = 5
# a = 6
# b = 4
# age = 13
# temperature = 20
# user_role ="admin"
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD" 
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "child" 
# weather = "HOT" if temperature > 20 else "Cold"
# access_level = "Full access" if user_role == "admin" else  "Limited Access"
# print(access_level)

# Concession stand program

# menu = {
#     "pizza": 3000,
#     "nachos": 450,
#     "popcorn": 600,
#     "fries": 2050,
#     "chips": 1000,
#     "pretzel": 350,
#     "soda": 300,
#     "lemonade": 400
# }

# cart = []
# total = 0

# print("-----------------MENU----------------")
# for key, value in menu.items():
#     print(f"{key:10}: {value: .2f}CFA")
# print("-------------------------------------")    


# while True:
#     food = input("Selecr an item or (q to quit): ")
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
        
# print("------------ YOUR ORDER ------------")        
# for food in cart:
#     total += menu.get(food) 
#     print(food, end=" ")
    
# print("-------------------------------------")    
# print(f"Total is: {total:.2f}CFA")        

# Python number guessing game
# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("--Welcome to Python Number Guessing Game")
# print(f"Select a number betweeb {lowest_num} and {highest_num}") 

# while is_running:
    
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
        
#         if guess < lowest_num or guess > highest_num:
#             print("Guess not found within given range")
#             print(f"Select a number betweeb {lowest_num} and {highest_num}") 
#         elif guess < answer:
#             print("Please Low, Try again!") 
#         elif guess > answer:
#             print("Too high, Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"You made {guesses} Number guesses")   
#             is_running = False        

#     else:
#         print("Invalid guess")
#         print(f"Select a number betweeb {lowest_num} and {highest_num}") 


# Rock paper, scissors game
import random

options = ("rock", "paper", "scissors")  
player = None
computer = random.choice(options)

player = input("Enter a choice (rock, paper, scissors)") 