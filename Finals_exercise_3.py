try:
    username = input("Enter username: ")
    age = int(input("Enter age: "))  

    if username.strip() == "" or age <= 0:
        raise ValueError("Invalid input.")

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("\nUser saved successfully.\n")

except ValueError:
    print("Error: Please enter a valid name and a positive number for age.")

except Exception as e:
    print("Unexpected error:", e)

try:
    print("\nSaved Users:")
    with open("users.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("\nNo users found yet.")

<<<<<<< HEAD:Finals_exercise_3.py
print("System complete.")
=======
print("System complete.")
>>>>>>> ce38fd6ffbac6eb79c5f7c49f935ecc8f88d59cf:Finals_exercise_3/Finals_exercise_3.py
