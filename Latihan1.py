import random

# Meminta input jumlah bilangan acak (n) dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

# Daftar untuk menyimpan bilangan acak yang lebih kecil dari 0.5
bilangan_acak_kecil = []

# Menggunakan while loop untuk terus menghasilkan bilangan acak hingga jumlahnya sesuai dengan n
while len(bilangan_acak_kecil) < n:
    bilangan = random.random()
    if bilangan < 0.5:
        bilangan_acak_kecil.append(bilangan)

# Menampilkan bilangan acak yang lebih kecil dari 0.5
print("Bilangan acak yang lebih kecil dari 0.5:")
for bilangan in bilangan_acak_kecil:
    print(bilangan)
