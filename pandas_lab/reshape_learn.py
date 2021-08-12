# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

men_women = oli[(oli.Edition == 2008) & ((oli.Event == '100m') | (oli.Event == '200m'))]

g = men_women.groupby(['NOC','Gender','Discipline','Event']).size()

df = g.unstack(['Discipline','Event'])

print(df)

print("Stack to make dataframe taller : ")
print(df.stack('Event'))

print("Unstack to make dataframe wider : ")
print(df.unstack('Gender'))