pembeli = str(input("Masukkan nama pembeli               : "))
noHp = str(input("Masukkan nomor hp                   : "))
kode = str(input("Masukkan kode jurusan               : ")).upper()
tiket = int(input("Masukkan jumlah tiket yang di pesan : "))

if kode in ("BLI"):
    kota = "Bali"
    harga = 300000
elif kode in ("DIY"):
    kota = "Yogyakarta"
    harga = 200000
elif kode in ("JKT"):
    kota = "Jakarta"
    harga = 350000
elif kode in ("LMP"):
    kota = "Lampung"
    harga = 500000
else:
    print("Maaf kode jurusan yang anda masukkan salah")
    exit()

total_pembayaran = harga * tiket
if tiket >= 3:
    diskon = total_pembayaran * 0.1
    total_bayar = total_pembayaran - diskon
else:
    total_bayar = total_pembayaran
    diskon = 0

print("=================================")
print("         HarapanSemua")
print("=================================")
print("Nama Pembeli    :", pembeli)
print("No. HP          :", noHp)
print("Kota Tujuan     :", kota)
print("Harga Satuan    : Rp.", harga)
print("Jumlah Tiket    :", tiket)
print("---------------------------------")
print("Diskon          : Rp.", diskon)
print("Total Bayar     : Rp.", total_bayar)
print("=================================")
print("Nikmati perjalanan Anda!")