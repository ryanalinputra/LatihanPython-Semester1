bil = 6  
while (bil < 5):  # 6 < 5 = False, jadi perulangan tidak dijalankan
    print("Bilangan ke - ", bil)  
    bil = bil + 1  
print("Selesai!")

print()  # Baris kosong

bil = 0  
while (bil < 5):  # Kondisi True selama bil < 5
    print("Bilangan ke - ", bil)  
    bil = bil + 1  # Increment bil setiap iterasi
print("Selesai!")

print()  # Baris kosong

bil = 0
while (bil < 5):  # Kondisi selalu True karena bil tetap 0
    print("Bilangan ke - ", bil)
    bil = bil  # nilai bil tidak bertambah dan akan berulang sampai kapanpun
    print("Selesai!")