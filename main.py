import random

def generate_random_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter an integer.")

def compare_numbers(user_guess, generated_number):
    if user_guess == generated_number:
        return "correct"
    elif user_guess > generated_number:
        return "high"
    else:
        return "low"

def main():
    lower_limit = 1
    upper_limit = 100
    generated_number = generate_random_number(lower_limit, upper_limit)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = get_user_guess()
        attempts += 1
        comparison_result = compare_numbers(user_guess, generated_number)

        if comparison_result == "correct":
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {generated_number} correctly in {attempts} attempts.")
        elif comparison_result == "high":
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")

if __name__ == "_main_":
    main()