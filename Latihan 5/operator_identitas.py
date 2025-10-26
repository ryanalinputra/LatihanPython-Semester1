a = 5
b = 5
# nilai a dan b sama, dan merujuk ke objek yang sama
print("a is b : ", a is b)      # Output: True
print("a is not b : ", a is not b)  # Output: False

list1 = [1, 2, 3]
list2 = [1, 2, 3]
# Meskipun nilai list1 dan list2 sama
# Keduanya adalah objek yang berbeda
print("list1 is list2 : ", list1 is list2)
# Output: False (dua objek terpisah)
print("list1 is not list2 : ", list1 is not list2)
# Output: True (objek yang berbeda)