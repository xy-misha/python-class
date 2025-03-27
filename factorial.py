# This program calculates the factorial of a given number using a loop.
# It will ask the user for a number and compute its factorial.
def factorial(n):
    """
    Function to calculate the factorial of a given number using a loop.
    :param n: The number whose factorial is to be calculated.
    :return: The factorial of n.
    """
    result = 1  # Initialize result as 1 since factorial of 0 is 1.
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive).
        result *= i  # Multiply result by the current number.
    return result  # Return the computed factorial.


# Display a welcome message to the user.
print("Welcome to the Factorial Calculation Program!")


# Loop to ensure valid user input.
while True:
    try:
        # Ask the user to enter a positive integer.
        num = int(input("Enter a positive integer to calculate its factorial: "))
        
        # Check if the entered number is negative.
        if num < 0:
            print("Factorial is not defined for negative numbers. Please enter a positive integer.")
        else:
            # Calculate and display the factorial.
            print(f"The factorial of {num} is {factorial(num)}")
            break  # Exit the loop once a valid number is provided.
    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please enter a valid positive integer.")
