file = open("students.csv", "r")

for line in file:
    parts = line.strip().split(",")
    name = parts[0]
    score = parts[1]
    print(f"Student: {name}\n Score: {score}")
    



file.close()