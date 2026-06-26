import random

while True:
    user = input("Roll the dice: (y/n): ").lower()

    if user == "y":
        first_num = random.randint(1, 6)
        second_num = random.randint(1, 6)
        print(f"({first_num}, {second_num})")
        print()

    elif user == "n":
        print('Thanks For Playing')
        break

    else:
        print("Please enter 'y' or 'n'.")
   