nilai = eval(input("Masukkan nilai: "))

if nilai >= 90:
    if nilai <= 100:
        print("Hasil ujian predikat A")
elif nilai >= 80:
    print("Hasil ujian predikat B")
elif nilai >= 60:
    print("Hasil ujian predikat C")
elif nilai >= 40:
    print("Hasil ujian predikat D")
else:
    print("Hasil ujian predikat E")