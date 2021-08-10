# SangTengkorak

# importing pandas library
import pandas as pd

print(pd.__version__)

# reading the csv file
df = pd.read_csv("data/olympics.csv")

# # reading the xlsx file
# df1 = pd.read_excel("data.xlsx")

print(df.head())

# print(df1.head())