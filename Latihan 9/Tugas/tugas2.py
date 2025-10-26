a = "*"  # Simbol yang akan dicetak

# Perulangan luar untuk mengontrol jumlah baris (1 sampai 5)
for i in range(1, 6):
    # Perulangan dalam untuk mencetak bintang sebanyak nilai i
    for j in range(i):
        print(a, end=' ')  # Cetak bintang dengan spasi, tanpa newline
    print()  # Pindah ke baris baru setelah selesai satu baris