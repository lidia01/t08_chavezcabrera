
#14
import libreria1
assert (libreria1.validar_mes("") == False)
assert (libreria1.validar_mes("chavez") == True)
assert (libreria1.validar_mes("cabrera") == False)
assert (libreria1.validar_mes("mujca") == True)
assert (libreria1.validar_mes("carrera") == False)
