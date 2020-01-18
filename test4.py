#04
import libreria1
assert (libreria1.entero("") == False)
assert (libreria1.entero(1) == False)
assert (libreria1.entero("1") == True)
assert (libreria1.entero(1) == False)
assert (libreria1.entero(1) == False)
print("entero OK")
