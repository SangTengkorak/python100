# SangTengkorak
import pandas as pd
import matplotlib.pyplot as plt
oli = pd.read_csv("data/olympics.csv", skiprows=4)

fo = oli[oli.Edition == 1896]

# plt.show(fo.Sport.value_counts().plot(kind="bar"))

# plt.show(fo.Sport.value_counts().plot(kind="line", figsize=(10,3)))

plt.show(fo.Sport.value_counts().plot(kind="pie", colormap="Pastel1")) 