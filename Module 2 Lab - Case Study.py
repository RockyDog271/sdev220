# Name: Rocky Duplexx
# App Name: Rocky's Honor Roll System
# Desc: App will ask for student name and GPA, then determine if they made the honor roll (GPA >= 3.5) or not (GPA < 3.5). App will continue to ask for students until user enters 'ZZZ' as last name. 

NonHonorStudent = ''
HonorListStudent = ''
HonorRollStudent = ''

while True == True:
    StudentLastName = str(input(f"Please enter the student's last name: "))
    if StudentLastName == 'ZZZ':
        quit()
    StudentFirstName = str(input(f"Please enter the student's first name: "))
    StudentGPA = str(input(f"Please enter the student's current GPA: "))

    if StudentGPA <= 3.25:
        if StudentGPA <= 3.5:
            print(f"{HonorRollStudent}")
        else:
            print(f"{HonorListStudent}")

    else:
        print(f"{NonHonorStudent}")


'''
Ask last name //StudentLastName
> if StudentLastName == 'ZZZ' then quit
Ask for first name //StudentFirstName
Ask for GPA (float) //StudentGrade

Logic here (see assignment)
Flag creation

print made or not made honor roll message
'''