def input_questions():
    # Prompt user for student's identification information...
    first = input('Please enter the student\'s first name. ')
    last = input('Please enter the student\'s last name. ')
    # Prompt user for student's contact information...
    address = input('Please enter the student\'s address. ')
    email = input('Please enter the student\'s email. ')
    phone = input('Please enter the student\'s phone_number. ')
    return[first, last, address, email, phone]


def create_student_dic():
    student = dict.fromkeys(['first_name', 'last_name',
                             'address', 'email', 'phone_number'])
    return student

