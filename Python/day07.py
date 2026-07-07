file = open("students.csv", "r")
next(file) #Ignore first line (The header of the csv)

total = 0
count = 0
for line in file:
    parts = line.strip().split(",")
    name = parts[0]
    score = int(parts[1])
    print(f"Student: {name}\n Score: {score} \n")
    total += score
    count += 1

average = total / count    
print(f"Average Score: {average}")


file.close()