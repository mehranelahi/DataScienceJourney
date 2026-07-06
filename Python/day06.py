file = open("students.txt", "r")

count = 0 
longest_name = ""

for line in file:
    print(line.strip())
    count += 1
    if len(line.strip()) > len(longest_name):
        longest_name = line.strip()
    
    
        
    
    
print(f"\nTotal Students: {count}")
print(f"Longest Name: {longest_name}")



file.close()

