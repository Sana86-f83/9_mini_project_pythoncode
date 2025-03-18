#Build Simple Calculator in python
print("\n=====================================")
print("\n📱 Simple Calculator 🧮")
print('''
➕  ADD
➖  SUBTRACT
✖️  MULTIPLY
➗  DIVIDE                  
''')

num1 = int(input("✅ Enter a First number here... " ))
num2 = int(input("✅ Enter a Second number here... " ))
oper = input("❇️  Select a operator here... (+, -, *, /) " )


if oper == "+":
    print("👤 user select operator is ",oper)
    print("➕ Add Result => ",num1 + num2)
elif oper == "-":
    print("👤 user select operator is ",oper)
    print("➖ Sub Result => ",num1 - num2)    
elif oper == "*":
    print("👤 user select operator is ",oper)
    print("✖️  Mult Result => ",num1 * num2)    
elif oper == "/":
    print("👤 user select operator is ",oper)
    if num2 == 0:
        print("❌ Error: Cannot divide by zero!")
    else:
        print("➗ Div Result => ",num1 / num2)
else:
    print("👤 user select operator is ",oper)
    print("❌ Invalid operator....")       

print("=====================================\n")
