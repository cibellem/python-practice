from typing import Dict

students = {
    "first_name": "none",
    "last_name": "none",
    "address": "none",
    "phone_number": "none"
}
students_list =[]

while True:

    first_name = input('Please enter the student\'s first name. ')
    last_name = input('Please enter the student\'s last name. ')

# Prompt user for student's contact information...
    address = input('Please enter the student\'s address. ')
    email = input('Please enter the student\'s email. ')
    phone_number = input('Please enter the student\'s phone_number. ')
# Print a separator...
    print('-' * 18)

    confirmation = input('Is this information correct? (y/n) ')

    if confirmation == "y":
        students_list.append({"first_name": first_name, "last_name": last_name,
                              "address": address, "phone_number": phone_number, "email": email})

        additional = input(
            "Would you like to add another student?(y/n)")
        if additional == "n":
            print(students_list)

        else:
               continue

    else:

        continue

# Print a separator...
print('-' * 9)