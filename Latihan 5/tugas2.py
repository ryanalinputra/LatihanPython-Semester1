import math
r = int(input("Masukkan jari-jari : "))
t = int(input("Masukkan tinggi : "))
L = 2 * math.pi * r * (r + t)
print("Hasil dari luas permukaan tabung adalah ", L ,)
V = math.pi * r**2
print("Hasil dari volume tabung adalah ", V)