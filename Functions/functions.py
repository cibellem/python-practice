from helpers import *

students = []
while True:
    first, last, address, email, phone = input_questions()
    student = create_student_dic(first_name=first, last_name=last,
                                 address=address, email=email,
                                 phone_number=phone)
