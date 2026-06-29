name = input("What's your name?")
age = input("How old are you?")
city = input("Where do you live?")

print("\n----- Your Info -----")
print(f"Hi {name}")
if int(age) > 18: 
    print(f"Age: {age} User is +18")
else:
    print(f"Age: {age} User is Under age")    

print(f"City: {city}")

