import random
import string
from colorama import Fore, Style  # For colored text output

def generate_password(length=12):
    """Generates a secure random password of given length."""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length > 25:
        print(Fore.RED + "\n⚠️ Error: Password length too high! Please enter a value below 25." + Style.RESET_ALL)
        return None
    elif length < 8:
        print(Fore.YELLOW + "\n⚠️ Warning: Password length too low! Please enter at least 8 characters for security." + Style.RESET_ALL)
        return None
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

# 🔹 User input
print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
length = int(input("🔐 Enter the length of your desired password: "))

# 🔹 Generate password
password = generate_password(length)

# 🔹 Display result
if password:
    print(Fore.GREEN + "\n✅ Your Secure Generated Password: " + Fore.YELLOW + password + Style.RESET_ALL)

print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
