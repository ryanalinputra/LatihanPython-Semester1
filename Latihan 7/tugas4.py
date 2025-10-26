nama_kasir = str(input("Masukkan nama kasir: "))
nama_pembeli = str(input("Masukkan nama pembeli: "))
total_belanja = int(input("Masukkan total belanja: Rp "))
nama_toko = "MAKMUR SENTOSA"
diskon = total_belanja * 0.2

if total_belanja >= 100000:
    print("Total Pembayaran: Rp", total_belanja - diskon)
else:
    print("Total Pembayaran: Rp", total_belanja)

print("Label Toko:", nama_toko)
print("Nama Kasir:", nama_kasir)
print("Nama Pembeli:", nama_pembeli)