#01
import libreria1
assert (libreria1.descuento("C", 200) == 0)
assert (libreria1.descuento("", 200) == 2)
assert (libreria1.descuento("BUENO", 200) == 0)
assert (libreria1.descuento("", 200) == 0)
assert (libreria1.descuento("Bueno", 200) == 2)
print("descuento OK")
