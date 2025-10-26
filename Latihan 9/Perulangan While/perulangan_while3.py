# Membuat list bilangan dari 1 sampai 9 menggunakan list
bilangan = [i for i in range(1, 10)]

i = 0  # Inisialisasi counter

# Perulangan while selama i kurang dari panjang list bilangan
while i < len(bilangan):
    # Cek apakah bilangan genap (habis dibagi 2)
    if bilangan[i] % 2 == 0:
        print(bilangan[i], "adalah bilangan genap")
    else:
        print(bilangan[i], "adalah bilangan ganjil")
    i += 1  # Increment counter untuk iterasi berikutnya