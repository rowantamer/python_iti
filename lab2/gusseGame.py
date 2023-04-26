import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    num_guesses = 10
    guessed_nums = set()
    
    while num_guesses > 0:
        # Get user input
        guess = input("Guess a number between 1 and 100: ")
        
        # Check if input is valid
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        guess = int(guess)
        
        # Check if number has already been guessed
        if guess in guessed_nums:
            print("You already guessed that number. Try again.")
            continue
        
        guessed_nums.add(guess)
        
        # Decrement remaining guesses
        num_guesses -= 1
        
        # Check if guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the secret number.")
            print("")
            return True
        
        # Give hint to user
        if guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        # Display number of remaining guesses
        print(f"You have {num_guesses} guesses left.\n")
    
    # If we get here, the user has used up all their guesses
    print("Game over! You ran out of guesses.")
    print(f"The secret number was {secret_number}.")
    print("")
    return False

while True:
    replay = input("Do you want to play a game? (y/n): ")
    if replay.strip().lower() == "y":
        play_game()
    else:
        print("Thanks for playing. Goodbye!")
        break
