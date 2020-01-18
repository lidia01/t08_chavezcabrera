
#14
def  validar mes(strApellido):
#el dedato es strMes es str
#la longitud de lacadena es al menos 5
if(isinstance(strMes,str)):
    if(len(strMes) >=5):
        return True     #es un apellido valido
    else:
        return False    #insuficientes caracteres
else:
    retur  False     #no es str
#Fin_validar_mes
