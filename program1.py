# Modal awal
modal_awal = 100000000  # 100 juta dalam rupiah

# Keuntungan bulanan dalam persentase
keuntungan_bulanan = [0, 0, 1, 1, 5, 5, 5, 3]

# Total keuntungan
total_keuntungan = 0

print("Keuntungan per bulan:")
# Looping untuk menghitung keuntungan setiap bulan
for i in range(8):
    keuntungan = modal_awal * (keuntungan_bulanan[i] / 100)
    total_keuntungan += keuntungan
    modal_awal += keuntungan
    # Tampilkan keuntungan bulan ke i+1
    print(f"Bulan {i+1}: {keuntungan} rupiah")

# Tampilkan total keuntungan
print("\nTotal keuntungan selama 8 bulan adalah:", total_keuntungan, "rupiah")
