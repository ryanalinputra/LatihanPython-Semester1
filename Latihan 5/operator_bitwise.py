# Angka dalam biner
a = 10   # 1010 dalam biner
b = 4    # 0100 dalam biner
# Operator Bitwise AND
result_and = a & b   # 1010 & 0100 = 0000 (0 dalam desimal)
print("AND:", result_and)
# Operator Bitwise OR
result_or = a | b    # 1010 | 0100 = 1110 (14 dalam desimal)
print("OR:", result_or)
# Operator Bitwise XOR
result_xor = a ^ b   # 1010 ^ 0100 = 1110 (14 dalam desimal)
print("XOR:", result_xor)
# Operator Bitwise NOT
result_not = ~a      # NOT 1010 = ...11110101 (two’s complement)
print("NOT:", result_not)
# Operator Shift Kiri
result_shift_left = a << 2   # 1010 << 2 = 101000 (20 dalam desimal)
print("Shift Kiri:", result_shift_left)
# Operator Shift Kanan
result_shift_right = a >> 1  # 1010 >> 21 = 0101 (5 dalam desimal)
print("Shift Kanan:", result_shift_right)