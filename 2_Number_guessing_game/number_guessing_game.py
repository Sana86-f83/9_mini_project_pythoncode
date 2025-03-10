import random

# Generate a random number between 1 and 10
com_number = random.randrange(1, 11)

# Get the user's guess
user_input = int(input("🎮 Enter a number between 1 and 10: "))

# Check if the user's guess is correct
if user_input > com_number:
    print("\n💻 Computer's number is:", com_number)
    print("📈 Your number is too high! Try again! 🚀")
elif com_number > user_input:
    print("\n💻 Computer's number is:", com_number)
    print("📉 Your number is too low! Try again! 🪂")
else:
    print("\n💻 Computer's number is:", com_number)
    print("🎉 Congratulations! You guessed the right number! 🏆")