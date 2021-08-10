# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

print(type(oli.index))

print(oli.head())

ath = oli.set_index('Athlete')

ath = ath.sort_index()

print(oli.iloc[1700])

print(oli.iloc[[1542, 2390, 6000, 15000]])

print(oli.iloc[1:4])