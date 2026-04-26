try:
    # Ask user input
    username = input("Enter username: ")
    age = int(input("Enter age: "))  # possible error if not a number

    # Validate input
    if username.strip() == "" or age <= 0:
        raise ValueError("Invalid input.")

    # Save to file
    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("\nUser saved successfully.\n")

except ValueError:
    print("Error: Please enter a valid name and a positive number for age.")

except Exception as e:
    print("Unexpected error:", e)

# Display all users from file
try:
    print("\nSaved Users:")
    with open("users.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("No users found yet.")

# Always display
print("System complete.")