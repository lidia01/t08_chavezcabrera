#06
def pedir_real(strMsg):
    num=""
    while(pedir_real(strMsg)==False):
        num=input(strMsg)
        if(pedir_formato_real(num)==True):
            num=float(num)
    #fin_while
    return num
#fin
