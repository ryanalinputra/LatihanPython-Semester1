nilai = int(input("Masukkan nilai siswa: "))

# Jika kondisi TRUE, pernyataan dibawahnya dieksekusi
if (nilai >= 85):
    print("Predikat A/Memuaskan")
# Jika kondisi pertama tidak TRUE, pernyataan dibawahnya dieksekusi
elif (nilai >= 75):
    print("Predikat B/Bagus")
#  Jika kondisi kedua tidak TRUE, pernyataan dibawahnya dieksekusi
elif (nilai >= 65):
    print("Predikat C/Cukup")
#  Jika kondisi ketiga tidak TRUE, pernyataan dibawahnya dieksekusi
elif (nilai >= 55):
    print("Predikat D/Kurang")
#  Jika kondisi semua tidak TRUE, pernyataan dibawahnya dieksekusi
else:
    print("Predikat E/Sangat Kurang")