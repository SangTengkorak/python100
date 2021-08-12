# SangTengkorak
import pandas as pd
import matplotlib.pyplot as plt

oli = pd.read_csv("data/olympics.csv", skiprows=4)

gu = oli[(oli.NOC == 'USA') & (oli.Medal == 'Gold')]

plt.show(gu.groupby(['Edition','Gender']).size().unstack('Gender',fill_value=0).plot())

gold = oli.groupby(['Athlete','Medal']).size().unstack('Medal', fill_value=0)

plt.show(gold.sort_values(['Gold', 'Silver', 'Bronze'], ascending=False)[['Gold', 'Silver', 'Bronze']].head().plot(kind='bar'))