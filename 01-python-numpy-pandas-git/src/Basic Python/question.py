def average_marks(total_marks,total_subject ):
    avg = total_marks/total_subject
    return avg
def highest_marks(list_of_marks):
    highest = 0
    for mark in list_of_marks:
        if mark > highest:
            highest = mark
    return highest

x = 0

while x != -1:
    no_of_students = int(input("Enter the number of students: "))
    for j in range(1,no_of_students+1):
        student_name = input(f"Enter the name of student#{j}: ")
        subjects = int(input("Enter the number of subjects: "))
        marks_list = []
        total = 0
        for i in range(1, subjects + 1):
            marks = int(input(f"Enter the marks of subject {i}: "))
            marks_list.append(marks)
            total += marks
        average = average_marks(total, subjects)
        highest_number = highest_marks(marks_list)
        print("The average marks are:", average)
        print("The highest marks are:", highest_number)
        print(student_name, ":", "Average Marks:", average, "Highest Marks:", highest_number)
    x = int(input("Enter -1 to exit or enter any other number to continue: "))
print("Program ended....")