# SangTengkorak
# April 06 2021

def is_prime(num):
    # Check from 2 to input number if there is any value that can divided with number aside of 1 and inputed number itself
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} not a prime')
            # stop division once condition not meet
            break
        else:
            print(f'{num} a prime')
            break

n = int(input('Please input number you want to check if prime : '))

is_prime(num=n)

n = int(input('Please input another number you want to check if prime : '))

is_prime(num=n)
