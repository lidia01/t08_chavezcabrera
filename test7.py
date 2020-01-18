#07
import libreria1
assert (libreria1.nombre("rosa") == 0)
assert (libreria1.nombre("ROSA") == 0)
assert (libreria1.nombre("Rosa") == 0)
assert (libreria1.nombre("") == 0)
assert (libreria1.nombre("rOS") == 0)
print("upper OK")
