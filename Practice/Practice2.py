import pandas as pd 

# data = {
#         "name":["Ali","Sara","Reza","Mehran"], 
#         "score":[18,20,9,19]
#  }

# df = pd.DataFrame(data)

# # print(df)


# passed_students = df[df["score"] >= 10][["name","score"]]
# # print(passed_students)

# failed_students = df[df["score"] < 10][["name","score"]]
# # print(failed_students)


# df["status"] = ["Pass","Pass","Fail","Pass"]
# print(df["status"].value_counts())


############################ Practice

data = {
        "name":["Ali","Sara","Reza","Mehran","Nima"],
        "department":["IT","HR","IT","Sales","IT"]
    }

df = pd.DataFrame(data)

# print(df)

# 1 
# print(df["department"].value_counts())

# 2
# print(df[df["department"] == "IT"])

# 3
employees_count = df["name"].count()
print(f"Total number of employees: {employees_count}")
