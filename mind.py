import random

def generate_random_number():
    return str(random.randint(1000, 9999))

def evaluate_guess(secret_number, guess):
    if guess == secret_number:
        return True
    else:
        correct_digits = sum(1 for a, b in zip(secret_number, guess) if a == b)
        print(f"Correct digits: {correct_digits}")
        return False

def player1_guess(secret_number):
    attempts = 0
    while True:
        guess = input("Player 1, make a guess: ")
        attempts += 1
        if evaluate_guess(secret_number, guess):
            print(f"Player 1 wins in {attempts} attempts!")
            return attempts

def player2_guess(secret_number):
    attempts = 0
    while True:
        guess = generate_random_number()
        attempts += 1
        if evaluate_guess(secret_number, guess):
            print(f"Player 2 wins in {attempts} attempts!")
            return attempts

def main():
    print("Welcome to the Mastermind game!")

    player1_wins = 0
    player2_wins = 0

    while True:
        secret_number = generate_random_number()
        print(f"Player 1, you're setting the number: {secret_number}")
        player1_attempts = player1_guess(secret_number)

        print("Switching roles...")

        secret_number = generate_random_number()
        print(f"Player 2, you're setting the number: {secret_number}")
        player2_attempts = player2_guess(secret_number)

        if player1_attempts < player2_attempts:
            player1_wins += 1
            print("Player 1 is crowned Mastermind!")
        else:
            player2_wins += 1
            print("Player 2 is crowned Mastermind!")

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print(f"Player 1 wins: {player1_wins}")
    print(f"Player 2 wins: {player2_wins}")

if __name__ == "__main__":
    main()