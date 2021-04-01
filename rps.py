#!/usr/bin/env python
# SangTengkorak
# Apr 1 2021

import random as rdm 

# RPS list for user and PC.
chall = ['Rock', 'Paper', 'Scissor']
defen = ['Rock', 'Paper', 'Scissor']

# Accept user input to call list index.
i_chall = (int(input('Please input your pick\n 1. Rock\n 2. Paper\n 3. Scissor\n : ')) - 1)

# Randomize PC choice
rani = rdm.randint(0, 2)
print(chall[i_chall])
print(defen[rani])

# RPS rule to output winner.
if i_chall == rani:
    print('Draw.')
if i_chall == 2 and rani == 0:
    print('You Lose.')
elif i_chall > rani:
    print('You Win.')
elif rani == 2 and i_chall == 0:
    print('You Win.')
elif rani > i_chall:
    print('You Lose.')
