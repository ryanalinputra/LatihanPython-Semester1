# Input I/O
bil1 = int(input("Masukkan Bilangan 1 = "))
bil2 = int(input("Masukkan Bilangan 2 = "))

# Jika kondisi TRUE, pernyataan dibawahnya dieksekusi
if (bil1 > bil2): # Kondisi
    hasil = "Besar" # Variable baru
    print("Besar")
# Jika kondisi FALSE, pernyataan dibawahnya dieksekusi
else: # Kondisi
    hasil = "Kecil" # Variable baru
    print("Kecil")

# Output
print("Bilangan", bil1, "lebih", hasil, "dari pada bilangan", bil2)