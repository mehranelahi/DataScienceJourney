import pandas as pd

df = pd.read_csv('students.csv')

print(df[['name', 'score']])

print(df[["name","status"]])

print(df[["score","status"]])

print(df[["status","name","score"]])