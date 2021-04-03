import string
import random as rdm


huruf = string.ascii_letters
angka = string.digits
simbol = string.punctuation

# Create password container
password = []

# Asks for password length and each of password element length
len_pass = int(input('How much caharacters you want for your password? '))

len_hur = int(input('how many letters you want? '))
len_pass = len_pass - len_hur

len_ang = int(input('how many numbers you want? '))
len_sim = len_pass - len_ang

print(f"For the rests of characters, we'll user {len_sim} symbols")

# Append every characters to password list, using for and range function
for i in range(len_hur):
  password.append(rdm.choice(huruf))

for i in range(len_ang):
  password.append(rdm.choice(angka))

for i in range(len_sim):
  password.append(rdm.choice(simbol))

# Shuffle password character list
rdm.shuffle(password)
print('This is your new password :')
print(''.join(password))