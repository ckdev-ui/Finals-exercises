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
    print("No users found yet.")

print("System complete.")