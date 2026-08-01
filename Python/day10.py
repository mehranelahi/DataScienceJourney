import pandas as pd

df = pd.read_csv("students.csv")

# print(df["score"] >= 18)

# mask = df["score"] >= 18 
# print(mask)
# print(df[mask])

# under_score = df["score"] < 18
# print(df[under_score])

# excellent = df["score"] == 20
# print(df[excellent])

# grade_b = df["score"] > 15
# print(df[grade_b]["name"])

# grade_a = (df["score"] >= 16) & (df["score"] <= 19)
# print(df[grade_a])

# darham = (df["score"] < 16) | (df["score"] == 20)
# print(df[darham])

# df.loc[df["name"] == "Ali", "score"] = 19
# print(df)

# df.loc[df["name"] == "Reza","score"] = 17
# print(df)

# df.loc[df["score"] < 18,"score"] = 18
# print(df)

# df["status"] = ""

df.loc[df["score"] >= 18,"status"] = "Pass"
df.loc[df["score"] < 18,"status"] = "Fail"

df.loc[df["score"] < 20, "score"] += 1

# print(df.sort_values("score"))

# print(df.sort_values("score", ascending=False))

# print(df.sort_values("score"))
# print(df.sort_values("score", ascending=False))
# print(df)

# sorted_df = df.sort_values("score")
# print(sorted_df)

# df = df.sort_values("name").reset_index(drop=True)
# print(df)

# print(df)

# df = df.sort_values("score", ascending=False)
# print(df)

# df = df.reset_index(drop=True)
# print(df)

