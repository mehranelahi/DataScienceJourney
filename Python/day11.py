import pandas as pd

df = pd.read_csv('students.csv')

# df["status"] = ""
df.loc[df["score"] >= 18, "status"] = "pass"
df.loc[df["score"] < 18,"status"] = "fail"

# print(df)

# print(df[['name', 'score']])

# print(df[["name","status"]])

# print(df[["score","status"]])

print(df[["status","name","score"]]) 