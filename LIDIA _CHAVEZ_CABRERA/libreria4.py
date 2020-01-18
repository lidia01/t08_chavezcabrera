#04
#funcion: devuelve numero entero
#param: strMsg0  mensaje para imput
#retorna: int
def pedir_entero(strMsg):
    num=""
    while(validar_entero(num)==False):
        num=input(strMsg)
        if(validar_formato_entero(num)==True):
            num=int(num)
    #fin_while
    return num
#fin
