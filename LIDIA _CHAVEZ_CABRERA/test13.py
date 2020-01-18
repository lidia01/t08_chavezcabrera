
#13
import libreria1
assert (libreria1.validar_mes("") == False)
assert (libreria1.validar_mes("enero") == False)
assert (libreria1.validar_mes("febrero") == True)
assert (libreria1.validar_mes("marzo") == True)
assert (libreria1.validar_mes("abril") == True)
