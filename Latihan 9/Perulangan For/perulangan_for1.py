# Perulangan pertama menampilkan angka 1 sampai 5
for a in [1, 2, 3, 4, 5]:
    print("Ini pengulangan ke -", a)

print()  # Baris kosong untuk pemisah

# Perulangan kedua menampilkan daftar makanan khas Indonesia
for b in ["Rawon", "Nasi kuning", "Soto", "Rendang", 
          "Lontong balap", "Ketoprak"]:
    print(b, "adalah masakan khas nusantara")

print()  # Baris kosong untuk pemisah

# Perulangan ketiga menghitung total dari list angka
angka = [4, 7, 2, 9, 1, 8, 0, 5]
total = 0
for hitung in angka:
    total = total + hitung  # Menambahkan setiap angka ke total
print("Jumlah keseluruhan:", total)