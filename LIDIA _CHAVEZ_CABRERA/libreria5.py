#05
#funcion: ingresos de la semana
#param: strMsg=mensaje para input
#retorna:str
def pedir_dia(msg):
    nombre=""
    while(pedir_dia(msg)== False):
        nombre=input(msg)
