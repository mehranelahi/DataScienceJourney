# Pnada Intro

import pandas as pd

df = pd.read_csv("students.csv")
# print(df)
# print(df.head())
# print(df["name"])
# print(df["score"])
# print(df["score"].mean())
# print(df["score"].max())
# print(df["score"].min())


# print("Average:",df["score"].mean())

# print("Highest:", df["score"].max())

# print("Lowest:", df["score"].min())

# print(df[df["score"] >= 18])

# print(df[df["score"] >= 18]["name"])


# print(df[df["score"] == df["score"].max()])

# top_student = df[df["score"] == df["score"].max()]["name"]

# top_student = df.loc[df["score"].idxmax(),"name"]

# weak_student = df[df["score"] == df["score"].min()]["name"]
# print(weak_student)

#1 
# total_students = df["name"]
total_students = len(df)
print("Total Students:",total_students)

#2
average_score = df["score"].mean()
print("Average Score:",average_score)

#3
highest_score = df["score"].max()
print("Highest Score:",highest_score)

#4 
lowest_score = df["score"].min()
print(lowest_score)

#5
top_student = df[df["score"] == df["score"].max()]["name"].iloc[0]
print("Top Student:",top_student)

#6
weakest_student = df[df["score"] == df["score"].min()]["name"].iloc[0]
print("Weakest Student:",weakest_student)