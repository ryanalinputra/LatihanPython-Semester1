i = 1
while i <= 4:        # Perulangan luar untuk baris (i dari 1 sampai 4)
    j = 0
    while j <= 3:    # Perulangan dalam untuk kolom (j dari 0 sampai 3)
        print(i*j, end=" ")  # Mencetak hasil perkalian i*j dengan spasi
        j += 1               # Increment j untuk kolom berikutnya
    print()          # Pindah ke baris baru setelah selesai satu baris
    i += 1           # Increment i untuk baris berikutnya