try:
    name = input("Enter student name: ")
    score = float(input("\nEnter score (0-100): ")) 

    if score < 0 or score > 100:
        print("\nInvalid score! ")
        print("Enter score between 0 and 100! ")
    else:
        if score >= 75:
            remarks = "Pass"
        else:
            remarks = "Fail"

        print("Student:", name)
        print("\nScore:", score)
        print("\nRemarks:", remarks)

except ValueError:
    print("\nInvalid input!")
    print("Please enter a valid numerical score between 0 and 100! ")

finally:
    print("\nEnd of Program.")