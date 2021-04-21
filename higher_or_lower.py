# Sangtengkorak
# April 21 2021

import random2 as rdm
from clear_screen import clear
from art import logo, vs
from game_data import data

print(logo)

# Create list for random medium
COMPETITOR = []
# User Score
SCORE = 0

# Add dictionary to list
for i in data:
    COMPETITOR.append(i)

# Create first compare
acak_1 = rdm.choice(COMPETITOR)
acak_1_fol = acak_1["follower_count"]

# Create second compare
acak_2 = rdm.choice(COMPETITOR)
acak_2_fol = acak_2["follower_count"]

def compare_question(acak_1, acak_2, vs):
    print(f"Compare A : {acak_1['name']}, a {acak_1['description']}, from {acak_1['country']}")
    print(vs)
    print(f"Compare B : {acak_2['name']}, a {acak_2['description']}, from {acak_1['country']}")

def comparing(acak_1_fol, acak_2_fol, choice):
    if choice == "A" and acak_1_fol > acak_2_fol:
        return True
    elif choice == "B" and acak_2_fol > acak_1_fol:
        return True
    else:
        return False

compare_question(acak_1, acak_2, vs)

# Take user input
choice = input("Who has more followers? Type 'A' or 'B': ")

# Comparing question with user input
result = comparing(acak_1_fol, acak_2_fol, choice)

while result == True:
    SCORE += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {SCORE}")
    acak_1 = acak_2
    acak_1_fol = acak_1["follower_count"]
    acak_2 = rdm.choice(COMPETITOR)
    acak_2_fol = acak_2["follower_count"]
    compare_question(acak_1, acak_2, vs)
    choice = input("Who has more followers? Type 'A' or 'B': ")
    result = comparing(acak_1_fol, acak_2_fol, choice)

print(f"Sorry, that's wrong. Final score: {SCORE}")
print(f"A Follower is : {acak_1_fol} mil")
print(f"B Follower is : {acak_2_fol} mil")
print(f"your choice is : {choice}")
print(result)
print(type(result))