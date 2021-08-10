# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

print(oli.shape)
# result in (Columns: 29216, Row: 10)

# print column shape
print(oli.shape[0])

# Print row shape
print(oli.shape[1])

# Print costum row and column
print(oli.head(10))

# info method
print(oli.info())