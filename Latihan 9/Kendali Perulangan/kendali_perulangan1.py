huruf = "ABCDEFG"
for periksa in (huruf):
    if periksa == "D":
        break  # Keluar dari perulangan ketika bertemu huruf 'D'
    print("Huruf saat ini : ", periksa)
print("Selesai!")
# Hanya mencetak huruf A, B, C lalu berhenti

print()  # Baris kosong

huruf = "ABCDEFG"
for periksa in (huruf):
    if periksa == "D":
        continue  # Lewati huruf 'D' dan lanjut ke iterasi berikutnya
    print("Huruf saat ini : ", periksa)
print("Selesai!")
# Mencetak semua huruf kecuali 'D'