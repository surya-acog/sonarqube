import random

def generate_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def get_guess():
    """Prompt the player to enter a guess."""
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Play the guessing game."""
    number_to_guess = generate_number()
    attempts = 0
    while True:
        attempts += 1
        guess = get_guess()
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

def main():
    """Main function to start the game."""
    print("Welcome to the Guessing Game!")
    play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
