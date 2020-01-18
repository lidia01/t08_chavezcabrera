#05
import libreria1
assert (libreria1.ingresos_de_la_semana("dia") == False)
assert (libreria1.ingresos_de_la_semana("dia") == True)
assert (libreria1.ingresos_de_la_semana("") == True)
assert (libreria1.ingresos_de_la_semana("Dia") == False)
assert (libreria1.ingresos_de_la_semana("dia") == False)
print("ingreso_de_la_semana OK")
