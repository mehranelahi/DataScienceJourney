


scores = []
student_names = []

def calculate_average(scores):
    return sum(scores) / len(scores)

new_student = "y"
while new_student == "y":
    
    student_name = input("Enter student's name: ")
    student_score = float(input("Enter student's score: "))
    scores.append(student_score)
    student_names.append(student_name)

    new_student = input("Add another student? (y/n): ").lower()
    
print("---- Report ----")
print(f'Total students: {len(student_names)} ')
print(f'Average score: {calculate_average(scores):.2f}')
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print("---- Student List ----")
for i in range(len(student_names)):
    print(f"{student_names[i]}: {scores[i]}")


