import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI Formula
    return round(bmi, 2)

# User Input
weight = float(input(Fore.GREEN + "\n🔹 Enter your weight in kg: "))
height = float(input(Fore.GREEN + "🔹 Enter your height in meters (e.g., 1.75): "))

# BMI Calculation
bmi = calculate_bmi(weight, height)

# Determine BMI Category
if bmi < 18.5:
    category = Fore.YELLOW + "⚠️  Underweight"
elif 18.5 <= bmi < 24.9:
    category = Fore.GREEN + "✅  Normal Weight"
elif 25 <= bmi < 29.9:
    category = Fore.MAGENTA + "⚠️  Overweight"
else:
    category = Fore.RED + "❌  Obese"

# Display Result
print(Fore.BLUE + "\n━━━━━━━━━━━━━━━━━━━━━━━")
print(Fore.YELLOW + f"📊  Your BMI is: {Fore.WHITE}{bmi}")
print(Fore.YELLOW + f"🏷  Category: {category}")
print(Fore.BLUE + "━━━━━━━━━━━━━━━━━━━━━━━\n")
