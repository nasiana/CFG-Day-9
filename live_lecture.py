# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Write a very simple encoding program that accepts a word from a user and encodes it by wrapping each letter with some
# other letters (symbols).

# exercise 1
meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

if meal_price > 20 and discount_applicable:
    final_price = 0.9 * meal_price
    print("Discount applied and the price is", str(final_price))
else:
    print("Discount not applied")

# exercise 2

pizza_temp = float(input("What's the temperature"))

if pizza_temp > 200:
    print("The oven is too hot")

elif pizza_temp == 180:
    print("The oven is at the perfect temperature")

elif pizza_temp < 150:
    print("The oven is too cold.")

else:
    print("The temperature is close enough.")

# exercise

def isPalindrome(string):
    if string == (string[::-1]):
       return True
    else:
       return False

print(isPalindrome('hannah'))  # should return True
print(isPalindrome('mummy'))  # should return False
print(isPalindrome('I'))  # should return True



    