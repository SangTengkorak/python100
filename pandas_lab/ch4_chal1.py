# SangTengkorak
import pandas as pd

oli = pd.read_csv("data/olympics.csv", skiprows=4)

# question 1
jowens = oli[oli.Athlete == "OWENS, Jesse"]
print(jowens.Event.value_counts)

# question 2
badminton_medalist = oli[(oli.Sport == "Badminton") & (oli.Gender == "Men")]
bad_country = oli[(oli.Event.str.contains("singles")) & (oli.Medal.str.contains("Gold")) & (oli.Discipline.str.contains("Badminton")) & (oli.Gender.str.contains("Men"))]
print(bad_country.sort_values(by="Athlete"))
print(badminton_medalist)

# question 3
recent_years = oli[oli.Edition >= 1984]
# Only display most top 3
print(recent_years.NOC.value_counts().head(3))

# question 4
hundred_sprint = oli[(oli.Gender.str.contains("Men")) & (oli.Discipline.str.contains("Athletics")) & (oli.Event.str.startswith("100m"))]
# Print only specified column, using list methode
print(hundred_sprint.sort_values(by=["Edition","City","Athlete","NOC"], ascending=False)[["City","Edition","Athlete","NOC"]])