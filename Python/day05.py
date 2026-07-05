# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     print(number)


# student_names = ["Ali","Sara","Reza"]

# for student in student_names:
#     print(student)

student_names = ["Ali","Sara","Reza"]
scores = [18,20,15]

print("----- Student List -----")

for i in range(len(student_names)):
    print(f"{student_names[i]}: {scores[i]}")



print("----- Statistics -----")

# Average score
average_score = sum(scores) / len(scores)
print(f"Average Score: {average_score}")

# Highest score
highest_score = max(scores)
print(f"Highest Score: {highest_score}")

# Lowest score
lowest_score = min(scores)
print(f"Lowest Score: {lowest_score}")

# Top student logic
highest_index = scores.index(max(scores))
top_student = student_names[highest_index]
print(f"Top Student: {top_student}")

# Passed and Faild Students
passed = 0
faild = 0
for score in scores:
    if((score * 5)  >= 70):
        passed += 1
    else:
        faild += 1
print(f"Passed Students: {passed}")
print(f"Faild Students: {faild}")




