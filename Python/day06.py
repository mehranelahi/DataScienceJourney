file = open("students.txt", "r")

count = 0 

for line in file:
    print(line.strip())
    count += 1
print(f"\nTotal Students: {count}")

file.close()


