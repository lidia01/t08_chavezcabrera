#09
import libreria1
assert (libreria1.replace("rosa", "lidia") == 0)
assert (libreria1.replace("rosa", "Lidia") == 0)
assert (libreria1.replace("ROSA", "LIDIA") == 0)
assert (libreria1.replace("", "LIDIA") == 0)
assert (libreria1.replace("ROSA", "lidia") == 0)
print("upper OK")
