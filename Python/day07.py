file = open("students.csv", "r")
next(file) #Ignore first line (The header of the csv)

total_score = 0
count = 0
highest_score = -1
lowest_score = 20
top_student = ""

for line in file:
    parts = line.strip().split(",")
    name = parts[0]
    score = int(parts[1])
    if score > highest_score:
        highest_score = score
        top_student = name
    if score < lowest_score:
        lowest_score = score

    print(f"Student: {name}\nScore: {score} \n")
    total_score += score
    count += 1

average = total_score / count    
print("\n----- Report -----")
print(f"\nAverage Score: {average:.2f}")
print(f"\nHighest Score: {highest_score}")
print(f"\nLowest Score: {lowest_score}\n")
print(f"Top Student: {top_student}")


file.close()