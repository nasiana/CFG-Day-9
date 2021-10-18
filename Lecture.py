### DEMO 1 ###
"""

float() can convert strings to floats

This code checks if the current temperature is freezing:
"""

temperature = input('What is the temperature? ')

is_freezing = float(temperature) <= 0.0

print('The temperature is freezing: {}'.format(is_freezing))


### EXERCISE 1 ###
"""
You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

Input the price of a burger using input()
Check whether the price is less than or equal (<=) 10.00
Print the result in the format below
Burger is within budget: True

Hint: remember to convert the input from a string to a decimal with float()

Example solution below.
"""

price = input('How much is a burger? ')

within_budget = float(price) <= 10.00

print('Burger is within budget: {}'.format(within_budget))

### DEMO 2 ###
"""
This program will work out if you should visit Mars based on whether you want to visit and if you can afford it.
"""

mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'

affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print('You should visit Mars: {}'.format(should_visit_mars))

### EXERCISE 2 ###
"""
Add code to your burger program to input whether the restaurant has a vegetarian option

The output should say whether the cost is within budget AND has a vegetarian option

    Restaurant meets criteria: True

See solution below
"""

price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')

within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'

is_good_choice = within_budget and has_vegetarian

print('Restaurant meets criteria: {}'.format(is_good_choice))

### DEMO 3 ###
"""

This program checks whether you are an admin and you have entered the right password:
"""

name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

if not is_admin or not is_password_correct:
    print('Go away')

### EXERCISE 3 ###
"""
Rewrite the output of your burger program to use if statements

If it is a good choice it should be:

    "This restaurant is a great choice!"

If it is not a good choice it should be:

    "Probably not a good idea"


Example solution below:
"""

price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')

within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'

is_good_choice = within_budget and has_vegetarian

if is_good_choice:
    print('This restaurant is a great choice!')

if not is_good_choice:
    print('Probably not a good idea')

### DEMO 4 ###
"""
Elif and Else statements explained with examples

Else EXAMPLE
"""
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

else:
    print('Go away')

"""
You can use multiple elif statements together.

Elif EXAMPLE
"""

dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')

elif dog_size < 10:
    print('That dog could fit in my pocket')

elif dog_size < 25:
    print('That is a small dog')

else:
    print('That is an average dog')

### EXERCISE 4 ###
"""

1 Else exercise:

Now that you've finished your burger, you want to pay for your food. 
Let's write a program to calculate your meal and apply a discount if applicable.
If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. 
The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.
"""

meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

### write your code here

'''
Example solution
'''
meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')

print('Total cost: {}'.format(meal_price))

"""
2 Elif Exercise:

You're cooking a pizza and need to check that the oven is at the right temperature.

Write a program to:

Ask the user to input the temperature
Prints "The oven is too hot" if the temperature is over 200
Prints "The oven is too cold" if the temperature is under 150
Prints "The oven is at the perfect temperature" if the temperature is 180
Prints "The temperature is close enough" for any other temperature
"""

# temperature = float(input('What is the temperature of the oven? '))
#
# ### your code goes here

'''
Example solution
'''

temperature = float(input('What is the temperature of the oven? '))

if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')

### DEMO 5 ###
"""
"""

import random

sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)

print('You rolled a {}'.format(random_integer))

### EXERCISE 5 ###
"""
This program uses random to simulate a coin flip.

To finish the program you will need to add the following:

If the random coin flip matches the choice input by the user then they win
Otherwise if the random coin flip does not match the choice input by the user then they lose
"""
# MY SOUTION

import random

def flip_coin():
    flip = random.randint(1,2)
    if flip == 1:
        outcome = 'heads'
    if flip == 2:
        outcome = 'tails'
    return outcome

choice = input('heads or tails: ')
result = flip_coin()

if choice == result:
    print("You win")
else:
    print("You lose")

print('The coin landed on {} and you picked {}.'.format(result, choice))


# Example solution

import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = input('heads or tails: ')
result = flip_coin()

print('The coin landed on {}'.format(result))
