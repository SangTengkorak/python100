# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

# Single Strings
print(oli[oli.Athlete.str.contains("Florence")])

# Multiple strings
print(oli[(oli.Athlete.str.contains("Florence")) & (oli.NOC.str.contains("USA"))])