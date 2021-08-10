# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

print(oli.shape)

ath = oli.Athlete.sort_values()

print(oli.sort_values(by=["Edition","Athlete"]))