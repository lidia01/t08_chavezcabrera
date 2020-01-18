#13
def  validar mes(strMes):
#el dedato es strMes es str
#la longitud de lacadena es al menos 6
if(isinstance(strMes,str)):
    if(len(strMes) >=6):
        return True #es un mes valido
    else
        return False #insuficientes caracteres
else:
    retur  False     #no es str
#Fin_validar_mes
