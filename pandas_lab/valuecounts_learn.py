# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

print(oli.Edition.value_counts())

print(oli.Gender.value_counts(ascending=True,dropna=False))