


print("\n==== Student Management System ====")
options = ["Show Report","Search Student","Show Excellebt Students","Show Passed Students","Show Failed Students","Exit"]

i = 1
for op in options:
    print(f"{i}. {op}")
    i += 1


def show_report():
    print("\n----- Report -----")
    file = open("students.csv","r")
    next(file)
    students = []
    scores = []
    top_student = ""
    weakest_student = ""
    for line in file:
        parts = line.strip().split(',')
        student_name = parts[0]
        student_score = int(parts[1])
        students.append(student_name)
        scores.append(student_score)
    print(f"Total Students: {len(students)}")
    print(f"Average Score: {(sum(scores) / len(scores)):.2f}")
    print(f"Highest Score: {max(scores)}")
    print(f"Lowest Score: {min(scores)}")

    highest_score = max(scores)
    for score in scores:
        if score > highest_score:
            highest_score = score
    top_student = students[scores.index(highest_score)]
    print(f"Top Student: {top_student}")
    
    lowest_score = min(scores)
    weakest_student = students[scores.index(lowest_score)]
    print(f"Weakest Student: {weakest_student}")


    file.close()
    

def search_student():
    question = str(input("Enter student's name: ")) 
    file = open("students.csv","r")
    students = []
    scores = []
    for line in file:
        parts = line.strip().split()
        student_name = parts[0]
        student_score = parts[1]
    students.append(student_name)
    scores.append(student_score)
    file.close()  

    if question in students:
        score = scores[students.index(question)]
        print(score)
    else:
        print("Student not found")




ask = int(input("What do you want? "))

if ask == 1:
    show_report()
elif ask == 2:
    search_student()
