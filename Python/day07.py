file = open("students.csv", "r")

for line in file:
    # print(line.strip())
    parts = line.split(",")
    print(parts)



file.close()