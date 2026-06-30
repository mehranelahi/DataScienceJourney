
scores = []
student_names = []
new_student = "y"
while new_student == "y":
    
    student_name = input("Enter student's name: ")
    student_score = int(input("Enter student's score: "))
    scores.append(student_score)
    student_names.append(student_name)

    new_student = input("Add another student? (y/n): ").lower()
    
print("---- Report ----")
print(f'Total students: {len(student_names)} ')
print(f'Average score: {sum(scores) / len(scores)}')
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")



