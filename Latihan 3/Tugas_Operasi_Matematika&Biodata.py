#Tugas Cek Integer
contoh_int1 = int (20)
contoh_int2 = int (300)
contoh_int3 = int (-13)
contoh_int4 = int (0o20)
contoh_int5 = int (-0o103)
contoh_int6 = int (-0o212)
contoh_int7 = int (0x56)

print(contoh_int1,contoh_int2,contoh_int3,contoh_int4,contoh_int5,contoh_int6,contoh_int7)

#Tugas Cek Float
contoh_float1 = float (0.1)
contoh_float2 = float (1.20)
contoh_float3 = float (-41.2)
contoh_float4 = float (32.23e123)
contoh_float5 = float (-92.)
contoh_float6 = float (-32.52e10)
contoh_float7 = float (60.2e-13)

print(contoh_float1,contoh_float2,contoh_float3,contoh_float4,contoh_float5,contoh_float6,contoh_float7)

#Tugas Cek Complex
contoh_complex1 = complex (3.14j)
contoh_complex2 = complex (35.j)
contoh_complex3 = complex (3.12e-12j)
contoh_complex4 = complex (.873j)
contoh_complex5 = complex (.123+0J)
contoh_complex6 = complex (3e+123J)
contoh_complex7 = complex (4.31e-4j)

print(contoh_complex1,contoh_complex2,contoh_complex3,contoh_complex4,contoh_complex5,contoh_complex6,contoh_complex7)

#Tugas Biodata 
nama = "Ryan Alin Putra"
alamat = "Dsn.Sumbersari RT03/RW06 Ds.Datengan Kec.Grogol Kab.Kediri"
usia = 19
no_hp = 6282140078266
jurusan = "D3-Manajemen Informatika"

print (
    "Nama    : " + nama + "\n" +
    "Alamat  : " + alamat + "\n" +
    "Usia    : " + str(usia) + "\n" +
    "No HP   : " + str(no_hp) + "\n" +
    "Jurusan : " + jurusan
)