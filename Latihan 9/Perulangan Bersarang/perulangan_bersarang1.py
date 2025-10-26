# List angka dan huruf
bilangan = [1, 2, 3]
huruf = ["A", "B"]

# Perulangan nested (bersarang)
for x in bilangan:      # Perulangan luar untuk setiap angka
    for y in huruf:     # Perulangan dalam untuk setiap huruf
        print(x, y)     # Mencetak kombinasi angka dan huruf