print("🍽️ Welcome to Python Restaurant 🍽️")
print("Please have a seat.\n")

while True:
    print("---- MENU ----")
    print("Press 1 for Burger 🍔")
    print("Press 2 for Coffee ☕")
    print("Press 3 for Tea 🍵")
    print("Press 4 for Other Food Items 🍕")
    print("Press 5 to Leave the Restaurant 🚪")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("You ordered a Burger 🍔\n")
        print("if you want anything else choode again from MENU")

    elif choice == "2":
        print("You ordered Coffee ☕\n")
        print("if you want anything else choode again from MENU")


    elif choice == "3":
        print("You ordered Tea 🍵\n")
        print("if you want anything else choode again from MENU")

    elif choice == "4":
        print("Other food items:")
        print("- Pizza 🍕")
        print("- Sandwich 🥪")
        print("- French Fries 🍟\n")

    elif choice == "5":
        print("Thank you for visiting! 😊")
        print("Have a nice day!")
        break

    else:
        print("Invalid choice ❌ Please select from 1 to 5.\n")
        print("thankyou\n")



