
# LISTS, DICTIONARIES AND CONDITIONALS #
students_list = []

while True:

    students = dict.fromkeys(["first_name", "last_name", "address", "phone_number"])
    students["first_name"] = input('Please enter the student\'s first name: ')
    students["last_name"] = input('Please enter the student\'s last name: ')

    # Prompt user for student's contact information...
    students["address"] = input('Please enter the student\'s address: ')
    students["email"] = input('Please enter the student\'s email: ')
    students["phone_number"] = input('Please enter the student\'s phone_number: ')
    # Print a separator...
    print('-' * 18)

    confirmation = input('Is this information correct? (y/n) ')
    if confirmation == "y":
        students_list.append(students)

        additional = input(
            "Would you like to add another student?(y/n)")
        if additional == "n":

            print('You\'ve entered the following student profiles:')
            print('-' * 18)
            for students in students_list:
                print('-' * 18)
                for key, value in students.items():
                    print(key, value)

            break

        else:
            continue

    else:

        continue
