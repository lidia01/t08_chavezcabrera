#06
import libreria1
assert (libreria1.num_real(1) == False)
assert (libreria1.num_real("1") == True)
assert (libreria1.num_real("1a") == True)
assert (libreria1.num_real(1) == True)
assert (libreria1.num_real("1M") == True)
print("num_real OK")
