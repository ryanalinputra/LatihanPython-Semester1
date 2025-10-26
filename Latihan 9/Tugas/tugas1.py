# Perulangan pertama: angka 1-14, melewati angka 5 dan 10
for a in range(1, 15):
    if a == 5:
        continue  # Lewati angka 5
    elif a == 10:
        continue  # Lewati angka 10
    elif a == 14:
        print(a, end="")  # Angka terakhir tanpa koma
    else:
        print(a, end=",")  # Angka dengan koma
print()  # Pindah baris

# Perulangan kedua: angka ganjil dari 1-19
for b in range(1, 21, 2):  # Step 2 untuk angka ganjil
    if b == 19:
        print(b, end="")  # Angka terakhir tanpa koma
    else:
        print(b, end=",")  # Angka dengan koma
print()  # Pindah baris

# Perulangan ketiga: kelipatan 5 dari 5-50
for c in range(5, 55, 5):  # Step 5 untuk kelipatan 5
    if c == 50:
        print(c, end="")  # Angka terakhir tanpa koma
    else:
        print(c, end=",")  # Angka dengan koma
print()  # Pindah baris