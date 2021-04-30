THR = int(input("Masukkan uang THR: Rp."))
THR_masuk = THR
pengeluaran = []
penggunaan = []

keep_run = 1

while keep_run > 0:
    item1 = int(input("Masukkan pengeluaran : Rp."))
    pengeluaran.append(item1)
    item2 = input("Pengguannya : ")
    penggunaan.append(item2)
    THR -= item1
    lanjut = input("Melanjutkan hitung?\n1. Ya\n2. Tidak\nPilihan: ")
    if lanjut == "1":
        keep_run = 1
    else:
        keep_run = 0

print(f"THR yang masuk : Rp.{THR_masuk}.")

for i, j in zip(pengeluaran, penggunaan):
    print(f"Setelah dikurangi : Rp.{i} untuk {j}")

print(f"Sisa THR : Rp.{THR}")