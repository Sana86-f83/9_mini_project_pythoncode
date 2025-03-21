import random

# User inputs a number secretly
print("\n","=" * 50)
user_number = int(input("👤 Enter a secret number (1-10) for the computer to guess: "))

attempts = 5  # Set max attempts
computer_guess = None

print("\n💻 Computer is guessing...")

for i in range(attempts):
    computer_guess = random.randint(1, 10)  # Computer makes a guess
    print(f"🔢 Attempt {i+1}: Computer guesses {computer_guess}")

    if computer_guess == user_number:
        print(f"\n🎉 The computer guessed your number {user_number} in {i+1} attempts! 🏆")
        break  # Exit the loop if guessed correctly
else:
    print(f"\n❌ The computer failed to guess your number {user_number} in {attempts} attempts! 😞")
