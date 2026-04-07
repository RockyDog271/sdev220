# Name: Rocky Duplexx
# App Name: Rocky's Honor Roll System
# Desc: App will ask for student name and GPA, then determine if they made the honor roll (GPA >= 3.5) or not (GPA < 3.5). App will continue to ask for students until user enters 'ZZZ' as last name. 

def NonHonorStudent(StudentFirstName, StudentLastName, StudentGPA):
    print(f"Sorry {StudentFirstName} {StudentLastName}, you did not make the honor roll with a GPA of {StudentGPA}.")

def HonorListStudent(StudentFirstName, StudentLastName, StudentGPA):
    print(f"Congratulations {StudentFirstName} {StudentLastName}, you made the honor list with a GPA of {StudentGPA}!")

def HonorRollStudent(StudentFirstName, StudentLastName, StudentGPA):
    print(f"Congratulations {StudentFirstName} {StudentLastName}, you made the honor roll with a GPA of {StudentGPA}!")

while True:
    # Input gathering
    StudentLastName = str(input(f"Please enter the student's last name: "))
    if StudentLastName == 'ZZZ':
        quit()
    StudentFirstName = str(input(f"Please enter the student's first name: "))

    # GPA input gathering
    try:
        StudentGPA = float(input(f"Please enter the student's current GPA: "))
    except ValueError:
        print(f"\nInvalid input for GPA. Please enter a numeric value.\n")
        continue

    # Minor Cleanup
    StudentLastName = StudentLastName.strip().title()
    StudentFirstName = StudentFirstName.strip().title()

    # Logic
    if StudentGPA >= 3.25:
        if StudentGPA >= 3.5:
            HonorRollStudent(StudentFirstName, StudentLastName, StudentGPA)
        else:
            HonorListStudent(StudentFirstName, StudentLastName, StudentGPA)
    else:
        NonHonorStudent(StudentFirstName, StudentLastName, StudentGPA)

    # Cleanup
    StudentLastName = ''
    StudentFirstName = ''
    StudentGPA = ''

'''
Ask last name //StudentLastName
if StudentLastName == 'ZZZ' then quit
Ask for first name //StudentFirstName
Ask for GPA (float) //StudentGrade

Logic here (see assignment)
Flag creation

print made or not made honor roll message
'''