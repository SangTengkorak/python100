# SangTengkorak
import pandas as pd
import matplotlib.pyplot as plt

oli = pd.read_csv("data/olympics.csv", skiprows=4)

noc = pd.read_csv("data/Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv")

plt.show(oli.Edition.value_counts().sort_index().plot())

print(noc.head())

print(noc[noc['Country'] != noc['Country.1']])

noc.set_index('Int Olympic Committee code', inplace=True)

print(noc.head())

lo = oli[oli.Edition == 2008]
medal_2008 = lo.NOC.value_counts()
print(medal_2008)

noc['medal_2008'] = medal_2008
print(noc[noc.medal_2008.isnull()])