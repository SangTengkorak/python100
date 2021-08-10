# SangTengkorak

import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)
print(oli.tail())