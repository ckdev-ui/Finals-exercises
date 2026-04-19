try:
    message = input("Enter a short message: ")
    
    with open("notes.txt", "w") as file:
        file.write(message + "\n")

    with open("notes.txt", "r") as file:
        print("\nContents of file: ")
        print(file.read())

    new_message = input("\nEnter another message: ")

    with open("notes.txt", "a") as file:
        file.write(new_message + "\n")

    with open("notes.txt", "r") as file:
        print("\nUpdated contents of file: ")
        print(file.read())

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print("An error occured:", e)