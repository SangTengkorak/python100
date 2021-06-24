# SangTengkorak
# June 24 2021

# Fungsi untuk memeriksa apakah angka termasuk bilangan prima atau bukan
def is_prime(y):
    # Dari angka 2 sampai angka yang dimasukkan diulang operasi pembagian
    for i in range(2, y):
        # Bila angka habis dibagi selain dengan angka itu sendiri maka tidak masuk bilangan prima
        if y % i == 0:
            return False
    # Mengeluarkan "True" untuk diolah lebih lanjut
    return True

# Menampung daftar angka prima
prime_list = []

# Menerima input angka
prime_suspect = int(input("Masukkan angka yang ingin di olah : "))

# Menggunakan fungsi yang telah dibuat untuk memeriksa apakah angka yang dimasukkan angka prima
prime_result = is_prime(prime_suspect)

# Dengan hasil yang dikeluarkan fungsi "True" atau "False", kita bisa menggunakan operasi kondisional
if prime_result == True:
    print(f"{prime_suspect} adalah bilangan prima.")
else:
    print(f"{prime_suspect} bukan bilangan prima.")

# Untuk memeriksa apakah mulai dari angka 1 sampai dengan angka yang dimasukkan ada bilangan prima apa saja
for i in range(1, prime_suspect+1):
    # prime_add adalah variable untuk ditambhakan ke list
    prime_add = is_prime(i)
    # Memeriksa satu persatu angka apakah habis dibagi selain angka itu sendiri
    if prime_add == True:
        # Bila kondisi sebagai angka prima terpenuhi, maka akan ditambahkan ke list.
        prime_list.append(i)

print(f"Bilangan Prima yang ada antara 1 sampai {prime_suspect}, adalah : ")
print(prime_list)

"""
Terima kasih banyak Lurs.
"""
