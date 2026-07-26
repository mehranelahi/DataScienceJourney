import pandas as pd

df = pd.read_csv("students.csv")

print("\n----- Student Report -----\n")

total_students = len(df["name"])
print("Total Students:",total_students)

average_score = df["score"].mean()
print("AverageScore:", average_score)

highest_score = df["score"].max()
print("Highest Score:",highest_score)

lowest_score = df["score"].min()
print("Lowest Score:", lowest_score)

top_student = df[df["score"] == df["score"].max()]["name"].iloc[0]
print("\nTop Student:",top_student)

weakest_student = df[df["score"] == df["score"].min()]["name"].iloc[0]
print("Weakest Student:",weakest_student)