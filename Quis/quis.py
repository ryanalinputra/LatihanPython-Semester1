namaKaryawan = str(input("Masukkan Nama Karyawan : "))
gajiPokok_usd = float(input("Masukkan Gaji Pokok : $ "))

idr = 16692.25
pajak = gajiPokok_usd * 0.10
asuransi = (gajiPokok_usd - pajak) * 0.03
iuranKoperasi = (gajiPokok_usd - pajak )
potongan = asuransi + pajak
gajiBersih = gajiPokok_usd - potongan
gajiPokok_idr = gajiPokok_usd * idr
pajak_idr = pajak * idr
asuransi_idr = asuransi * idr
potongan_idr = potongan * idr
gajiBersih_idr = gajiBersih * idr


print("Nama Karyawan : ", namaKaryawan,
      "\nGaji Pokok : Rp.", gajiPokok_idr,
      "\nPajak : Rp.", pajak_idr,
      "\nAsuransi : Rp.", asuransi_idr,
      "\nPotongan : Rp.", potongan_idr,
      "\nGaji Bersih : Rp.", gajiBersih_idr
      )