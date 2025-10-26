# Input I/O
nilai = int(input('Masukkan nilai: '))
usia = int(input('Masukkan usia: '))

# Jika kondisi TRUE, pernyataan dibawahnya dieksekusi
if nilai >= 75: # Kondisi
    if usia < 15: # Kondisi
        print('Selamat adek, kamu lulus!')
    else: # Kondisi
        print('Selamat kakak, kamu lulus!')
# Jika kondisi FALSE, pernyataan dibawahnya dieksekusi
else: # Kondisi
    if usia < 15: # Kondisi
        print('Mohon maaf dek, coba lagi ya!')
    else: # Kondisi
        print('Mohon maaf kak, coba lagi ya!')