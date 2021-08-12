# SangTengkorak
import pandas as pd
import matplotlib.pyplot as plt

oli = pd.read_csv("data/olympics.csv", skiprows=4)

# Create groupby objet
oli.groupby('Edition')

# # Display groupby objet content
# print(list(oli.groupby('Edition')))

# # Iterate through groupby object
# for group_key, group_value in oli.groupby('Edition'):
#     print(group_key)
#     print(group_value)

# # View groupby object size
# print(oli.groupby('Edition').size())

# print(oli.groupby(['Edition','NOC','Medal']).size())

# print(oli.groupby(['Edition','NOC','Medal']).agg({'Edition' :['min','max','count']}))

print(oli.loc[oli.Athlete == 'LEWIS, Carl'].groupby('Athlete').agg({'Edition' : ['min','max','count']}))