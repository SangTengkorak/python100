def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} not a prime')
            break
        else:
            print(f'{num} a prime')
            break

n = int(input('Please input number you want to check if prime : '))

is_prime(num=n)

n = int(input('Please input another number you want to check if prime : '))

is_prime(num=n)