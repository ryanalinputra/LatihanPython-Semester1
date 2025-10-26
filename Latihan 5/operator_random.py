# Fungsi choie
import random
buah = ["apel", "ceri", "jeruk", "mangga", "kiwi"]
print(random.choice(buah))

# Fungsi choice randrange
print("Nilai random dari 0 s.d. 100 : ", random.randrange(100))
print("Nilai random dari 50 s.d. 100 : ", random.randrange(50,100))
print("Nilai random dari 0 s.d. 100 kelipatan 5 : "
      , random.randrange(50,100,5))

# Fungsi random 
from random import random
print(random())

# Fungsi seed
import random
random.seed(3)
print(random.randint(1, 1000)) #membangkitkan nilai random
random.seed(3)                 #mengunci nilai random
print(random.randint(1, 1000)) #membangkitkan nilai random
                               #tetapi terkunci oleh fungsi seed
print(random.randint(1, 1000)) #membangkitkan nilai random kembali

#Fungsi shuffle
import random
buah = ["apel", "ceri", "jeruk", "mangga", "kiwi"]
random.shuffle(buah)
print(buah)