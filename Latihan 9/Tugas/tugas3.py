max_baris = 7    # Jumlah maksimal baris
max_kolom = 7    # Jumlah maksimal kolom

baris = 0  
while baris < max_baris:      # Perulangan untuk setiap baris
    kolom = 0  
    while kolom < max_kolom:  # Perulangan untuk setiap kolom dalam baris
        # Cetak "o" jika kolom <= baris, cetak "*"
        print("o" if kolom <= baris else "*", end = " ")
        kolom += 1  
    else:  
        print (" ")  # Pindah baris setelah selesai satu baris
    baris += 1  