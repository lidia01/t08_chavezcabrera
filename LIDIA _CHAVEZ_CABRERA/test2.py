#02
import libreria1
assert (libreria1.emergencia("ROJO") == 0)
assert (libreria1.emergencia("Rojo") == 0)
assert (libreria1.emergencia("rOJO") == 0)
assert (libreria1.emergencia("Roj") == 0)
assert (libreria1.emergencia("") == 0)
print("emergencia OK")
