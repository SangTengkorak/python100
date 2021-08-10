# SangTengkorak

import pandas as pd

# Create dataframe from panda read_csv method.
oo = pd.read_csv("data/olympics.csv", skiprows=4)

# Display ends of dataframe
print(oo.tail())

# Print only specific series
print(oo["Athlete"])
print(oo.Medal)
print(oo[["City"]])
print(oo[["City","Athlete","Gender","Event"]])