i = 1
while i < 56:
    print(i)
    if i == 3:
        break  # Menghentikan perulangan ketika i == 3
    i += 1
print("Selesai!")
# Perulangan berhenti di angka 3 meskipun kondisi while i < 56

print()  # Baris kosong

i = 0
while i < 5:
    i += 1  # Increment i di awal untuk menghindari infinite loop
    if i == 3:
        continue  # Melewati iterasi ketika i == 3
    print(i)
print("Selesai!")
# Angka 3 tidak dicetak karena dilewati oleh continue