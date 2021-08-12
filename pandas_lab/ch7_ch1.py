# SangTengkorak
import pandas as pd
import matplotlib.pyplot as plt

oli = pd.read_csv("data/olympics.csv", skiprows=4)

# Total medal per-edition
plt.show(oli.groupby('Edition').size().plot())


print(oli.groupby('NOC').agg({'Edition' : ['count','min','max']}))