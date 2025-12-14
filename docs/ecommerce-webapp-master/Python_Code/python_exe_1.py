# 1. Odd or Even
# Write a Python program that takes an integer as input from the user and prints "Even" if the number is even, 
# and "Odd" if it is odd.

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Voting Eligibility
# Write a program that asks for a user's age. If the user is 18 or older, print "You are eligible to vote." 
# Otherwise, print "You are not eligible to vote yet."

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# 3. Number Comparison
# Write a program that takes two numbers as input and prints:
# "The first number is greater." if the first number is larger.
# "The second number is greater." if the second number is larger.
# "Both numbers are equal." if they are the same.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")


# 4. Simple Calculator
# Write a program that asks the user to input two numbers and an operator (+, -, *, /). 
# Based on the operator provided, calculate and print the result. Make sure to handle division by zero.

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    print(f"The result is: {num1 + num2}")
elif operator == '-':
    print(f"The result is: {num1 - num2}")
elif operator == '*':
    print(f"The result is: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")


# 5. Grade Calculator
# Create a program that asks for a student's score (0–100).
# If the score is 90 or above, print "A".
# If the score is between 80 and 89, print "B".
# If the score is between 70 and 79, print "C".
# If the score is between 60 and 69, print "D".
# If the score is below 60, print "F".

score = float(input("Enter the student's score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# 6. Leap Year Checker
# Write a program that checks if a given year is a leap year. A leap year is divisible by 4 but not by 100, 
# except when it is also divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# 7. Positive, Negative, or Zero
# Write a program that takes a number as input and prints "Positive" if the number is greater than zero, 
# "Negative" if it is less than zero, and "Zero" if it is exactly zero.

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 8. Day of the Week
# Write a program that takes an integer (1 to 7) from the user and prints the corresponding day of 
# the week (1 = Monday, 2 = Tuesday, etc.). If the number is not between 1 and 7, print "Invalid day".

day = int(input("Enter a number (1-7) for the day of the week: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

# 9. Largest of Three Numbers
# Write a program that takes three numbers as input and prints the largest of the three. 
# Make sure to handle cases where two or more numbers are equal.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)

if num1 == num2 == num3:
    print("All numbers are equal.")
else:
    print(f"The largest number is: {largest}")


# 10. Rock, Paper, Scissors Game
# Write a simple two-player Rock, Paper, Scissors game. Both players input their choice, and 
# the program determines the winner (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).

player1 = input("Player 1, enter your choice (Rock, Paper, Scissors): ").lower()
player2 = input("Player 2, enter your choice (Rock, Paper, Scissors): ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
