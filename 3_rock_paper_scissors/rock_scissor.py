import random

selec_option = "🪨 rock", "✂️ scissor", "📃 paper"

while True:
    uCount = 0
    cCount = 0
    user_choice = int(input('''
🎮 Game Start 🎯
1 -- Yes
2 -- No | Exit

'''))

    if user_choice == 1:
        for a in range(1, 6):
            user_input = int(input('''
1 🪨  Rock
2 ✂️  Scissor
3 📃  Paper

'''))
            if user_input == 1:
                uChoice = "🪨 rock"
            elif user_input == 2:
                uChoice = "✂️ scissor"
            elif user_input == 3:
                uChoice = "📃 paper"

            Com_choice = random.choice(selec_option)

            if Com_choice == uChoice:
                print("Computer Value:", Com_choice)
                print("Your Value:", uChoice)
                print("Game Draw 🤝")
                uCount = uCount + 1
                cCount = cCount + 1
            elif (uChoice == "🪨 rock" and Com_choice == "✂️ scissor") or (uChoice == "📃 paper" and Com_choice == "🪨 rock") or (uChoice == "✂️ scissor" and Com_choice == "📃 paper"):
                print("Computer Value:", Com_choice)
                print("Your Value:", uChoice)
                print("You Win 💥")
                uCount = uCount + 1
            else:
                print("Computer Value:", Com_choice)
                print("Your Value:", uChoice)
                print("Computer Win 😩")
                cCount = cCount + 1

        if uCount == cCount:
            print("Final Game Draw... 🤝")
            print("User Score:", uCount)
            print("Computer Score:", cCount)
        elif uCount > cCount:
            print("Final You Win the Game 🎉")
            print("User Score:", uCount)
            print("Computer Score:", cCount)
        else:
            print("Final Computer Win the Game 😩")
            print("User Score:", uCount)
            print("Computer Score:", cCount)

    else:
        break