# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

# Single condition
print(oli[oli.Medal == "Gold"])

# Multiple conditions
print(oli[(oli.Medal == "Gold") & (oli.Gender == "Women")])