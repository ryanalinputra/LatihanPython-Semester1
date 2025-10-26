hari = str(input("Masukkan Hari: "))

if hari in ["senin","selasa","rabu","kamis","jumat"]:
    print("Hari Kerja")
elif hari in ["sabtu","minggu"]:
    print("Hari Libur")
else:
    print("mohon isi dengan format yang benar")