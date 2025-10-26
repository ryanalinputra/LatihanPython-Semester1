bil = int(input("Masukkan angka selain 0: ")) # Meminta input angka pertama dari user

while bil != 0: # Perulangan while selama angka yang dimasukkan bukan 0
    print(bil, "Bukan angka 0")
    bil = int(input("Masukkan angka selain 0: ")) # Meminta input angka berikutnya

# Program keluar dari perulangan ketika user memasukkan angka 0
print("Yang anda masukkan angka 0")