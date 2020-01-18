
#10
import libreria1
assert (libreria1.replace("uno", "dos") == 0)
assert (libreria1.replace("UNO", "dos") == 0)
assert (libreria1.replace("uno", "DOS") == 0)
assert (libreria1.replace("Uno", "Dos") == 0)
assert (libreria1.replace("", "dos") == 0)
print("replace OK")
