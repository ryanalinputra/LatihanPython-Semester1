# Program untuk mengecek bilangan prima dari 1 sampai 9
for i in range(1, 10):
    pembagi = 0
    # Menghitung jumlah pembagi
    for j in range(1, i+1):
        sisa_bagi = i % j
        if sisa_bagi == 0:
            pembagi = pembagi + 1
    # Cek jika bilangan prima (hanya punya 2 pembagi)
    if pembagi == 2:
        print(i, "adalah bilangan prima")
    else:
        print(i, "bukanlah bilangan prima")