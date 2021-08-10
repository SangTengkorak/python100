# SangTengkorak

import pandas as pd

# List Olimpycs DataFrame
oli = pd.read_csv("data/olympics.csv", skiprows=4)

print(oli["NOC"])
print(type(oli.NOC))

print(oli[["Edition","City","Athlete","Medal"]])
print(type(oli[["Edition","City","Athlete","Medal"]]))