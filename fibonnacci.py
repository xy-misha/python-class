# This program calculates and prints the Fibonacci sequence up to a given number.
# It will ask the user for their name and greet them before continuing.
# Ask the user for their name and store it in the variable 'name'
name = input("What is your name? ")
# This is a Fibonacci program.
# This program will ask the user for a number and then print the Fibonacci sequence up to that number.

def fibonacci(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def get_positive_integer():
    """Prompts the user for a positive integer input and validates it."""
    while True:
        try:
            # Ask the user for input and convert it to an integer.
            n = int(input("How many Fibonacci terms would you like to generate? Please enter a positive integer: "))
            # Ensure the user enters a positive integer.
            if n > 0:
                return n
            else:
                print("Please enter a positive integer greater than zero.")
        except ValueError:
            # Handle invalid input (e.g., letters or symbols instead of numbers).
            print("Invalid input. Please enter a positive integer.")


def main():
    """Main function to welcome the user, get the number of terms, and generate the Fibonacci sequence."""
    # Print a welcome message for the user.
    print(f"Welcome, {name}, to the Fibonacci Sequence Generator!")
    
    # Get the number of terms the user wants.
    n_terms = get_positive_integer()
    
    # Inform the user that the sequence is being generated.
    print(f"\nFibonacci sequence up to the {n_terms}-th term:")
    
    # Generate and print the Fibonacci sequence up to the given number of terms.
    for i in range(n_terms):
        print(f"Term {i + 1}: {fibonacci(i)}")
    print()  # Move to a new line after printing the sequence.


# This ensures the script runs only if executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
