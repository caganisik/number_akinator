import random

def guess_number(lower_bound=1, upper_bound=100):
    
    print(f"Think of a number between {lower_bound} and {upper_bound}.")

    # Initialize the search space
    low = lower_bound
    high = upper_bound
    num_guesses = 0

    while low <= high:
        num_guesses += 1
        # Use binary search to make an educated guess
        guess = (low + high) // 2
        print(f"My guess is: {guess}")

        # Get feedback from the user
        feedback = input("Is it higher, lower, or correct? (h/l/c): ")

        if feedback.lower() == 'h':
            low = guess + 1
        elif feedback.lower() == 'l':
            high = guess - 1
        else:
            print(f"Yay! I guessed your number in {num_guesses} guesses.")
            return

    print("Something went wrong. Please try again.")

if __name__ == "__main__":
    guess_number()