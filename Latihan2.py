# Inisialisasi variabel untuk menyimpan bilangan terbesar
bilangan_terbesar = None

# Perulangan untuk menerima input dari pengguna
while True:
    bilangan = float(input("Masukkan sebuah bilangan (masukkan 0 untuk berhenti): "))
    
    # Jika pengguna memasukkan 0, keluar dari loop
    if bilangan == 0:
        break
    
    # Periksa apakah bilangan saat ini lebih besar dari bilangan terbesar
    if bilangan_terbesar is None or bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

# Tampilkan bilangan terbesar jika ada
if bilangan_terbesar is not None:
    print("Bilangan terbesar adalah:", bilangan_terbesar)
else:
    print("Tidak ada bilangan yang dimasukkan.")
