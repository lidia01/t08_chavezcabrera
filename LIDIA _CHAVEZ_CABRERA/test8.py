#08
import libreria1
assert (libreria1.upper("alex") == 0)
assert (libreria1.upper("alexis") == 0)
assert (libreria1.upper("ALEXIS") == 0)
assert (libreria1.upper("") == 0)
assert (libreria1.upper("Ale") == 0)
print("upper OK")
