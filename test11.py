#11
import libreria1
assert (libreria1.descuento("R", 300) == 0)
assert (libreria1.descuento("", 300) == 3)
assert (libreria1.descuento("RAPIDO", 300) == 0)
assert (libreria1.descuento("", 300) == 0)
assert (libreria1.descuento("Rapido", 300) == 3)
print("descuento OK")
