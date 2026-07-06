file = open("students.txt", "r")

count = 0 
longest_name = ""
shortest_name = ""


for line in file:
    line = line.strip()
    print(line)
    count += 1
    if len(line) > len(longest_name):
        longest_name = line

    if  shortest_name == "" or len(line) < len(shortest_name):
        shortest_name = line
    
    
    
print(f"\nTotal Students: {count}")
print(f"Longest Name: {longest_name}")
print(f"Shortest Name: {shortest_name}")


file.close()

