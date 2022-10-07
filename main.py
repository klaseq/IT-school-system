from itsystem import ITSystem
from person import Teacher

def print_menu():
    print("\n############################")
    print("Welcome in system")
    print("Press button: ")
    print("\t 0 to add a teacher")
    print("\t 1 to add a course")
    print("\t 2 to add a student")
    print("\t 3 to teacher list")
    print("\t 4 to course list")
    print("\t 5 to student list")
    print("\t 6 to exit")

it_system = ITSystem()

while True:
    print_menu()
    try:
        menu_select = int(input("Menu select: "))
        if menu_select < 0 or menu_select >= 7:
            raise Exception("Wrong number of menu")
    except Exception as e:
        print(e)
        print("Please select valid number")
    if menu_select == 6:
        print("Good bye")
        break
    elif menu_select == 0:
        it_system.create_teacher()
    elif menu_select == 1:
        if len(it_system.teachers) <= 0:
            print("Your teacher list is empty, first you have to add a teacher")
        else:
            it_system.create_course()
    elif menu_select == 2:
        if len(it_system.teachers) <= 0 or len(it_system.courses) <= 0:
            print("Your teacher or course list is empty, first you have to add a teacher and a course")
        else:
            it_system.create_student()
    elif menu_select == 4:
        print("Course list:")
        for course in it_system.courses:
            print(course)
    elif menu_select == 5:
        print("Student list:")
        for student in it_system.students:
            print(student)
    elif menu_select == 3:
        print("Teacher list:")
        for teacher in it_system.teachers:
            print(teacher)

