def show_report():
    print("\n----- Student Management System -----")
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
    top_student = students[scores.index(highest_score)]
    print(f"Top Student: {top_student}")
    
    lowest_score = min(scores)
    weakest_student = students[scores.index(lowest_score)]
    print(f"Weakest Student: {weakest_student}")


    file.close()
    

def search_student(): 
    file = open("students.csv","r")
    next(file)
    students = []
    scores = []

    for line in file:
        parts = line.strip().split(',')
        name = parts[0]
        score = int(parts[1])
        students.append(name)
        scores.append(score)

    student_name = input("Enter student's name: ")

    if student_name in students:
        student_index = students.index(student_name)
        student_score = scores[student_index]
        print(f"{student_name}'s score is {student_score}")
    else:
        print("Student not found")
    file.close()  


def show_excellent():
    file = open("students.csv",'r')
    next(file)

    for line in file:
        parts = line.strip().split(',')
        name = parts[0]
        score = int(parts[1])
        if score >= 18:
            print(f'{name} --> {score}') 
   
    file.close()

def show_passed():
    print("\n----- Passed Students -----")
    file = open("students.csv","r")
    next(file)

    for line in file:
        parts = line.strip().split(',')
        name = parts[0]
        score = int(parts[1]) 
        if score >=10:
            print(f"{name}")
        else:
            print("----- Failed Students -----")
            print(f"{name}")
    file.close()


while True:
 print("\n==== Student Management System ====")
 options = ["Show Report","Search Student","Show Excellent Students","Show Passed Students / Failed Students","Exit"]

 i = 1
 for op in options:
     print(f"{i}. {op}")
     i += 1

 ask = int(input("What do you want? "))

 if ask == 1:
     show_report()
 elif ask == 2:
     search_student()
 elif ask == 3:
     show_excellent()
 elif ask == 4:
     show_passed()
 elif ask == 5:
     print("Goodbye👋")
     break
 else:
     print("Invalid choice. Please try again.")
