num1 = float(input("Enter first number: ")) #declairing first variable to get float input from user
num2 = float(input("Enter second number: ")) #declairing second variable to get float input from user
operator = input("Enter an operator: ") #declaring third variable to get operator input from the user
if operator == "+": #using if, elif and else conditions to check multiple opearotrs and give output
    print(f"First number is {num1}")
    print(f"\nSecond number is {num2}")
    print(f"\nSum is: {num1+num2}")
elif operator == "-":
    print(f"First number is {num1}")
    print(f"\nSecond number is {num2}")
    print(f"\nSubtract is: {num1-num2}")
elif operator == "*":
    print(f"First number is {num1}")
    print(f"\nSecond number is {num2}")
    print(f"\nMultiplication is: {num1*num2}")
elif operator == "/":
    print(f"First number is {num1}")
    print(f"\nSecond number is {num2}")
    print(f"\nDivision is: {num1/num2}")
elif operator == "%":
    print(f"First number is {num1}")
    print(f"\nSecond number is {num2}")
    print(f"\nModulus is: {num1%num2}")
else:
    print("\nPlease enter a valid operator!") #printing a final message if operator is wrong
