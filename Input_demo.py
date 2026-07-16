name = input("Enter your name: ")

if name == "Jaspreet":
    print("Hey Jaspreet Singh, welcome back!")
    print("You are an engineer by profession.")
    print("How is your Python learning journey going?")

elif name == "Gurpal":
    print("Hey Gurpal, welcome back!")
    print("You are a teacher by profession.")
    print("How is your lecturer exam preparation going?")

else:
    print("Sorry, you are not registered in the system.")
    register= input("Would you like to register? (yes/no): ")
    if register == "yes":
        name = input("Please enter your name: ")
        profession = input("Please enter your profession: ")
        print("Thank you for registering", name)
        print("You are now registered as a", profession)
    else:
        print("Thank you for visiting. Have a great day!")