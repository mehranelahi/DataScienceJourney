file = open("practice1.csv",'r')
next(file)

total_students = 0

for line in file:
    parts = line.strip().split(',')
    student_name = parts[0]
    student_score = parts[1]
    total_students += 1
    print(f"{student_name} --> {student_score}")

print("----- Report -----")
print(f"\nTotal Students: {total_students}")

file.close()