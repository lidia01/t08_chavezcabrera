#11
#si el tipo de servicio internet
#aqui una funcion upper
def descuento (tipo,prestamo):
    if (tipo.upper()== "RAPIDO"):
        return 0.30 * prestamo
    else:
        return 0
def reporte_prestamo(nombre,precio,descuento):
    print("############################")
    print("#reporte de prestamo#")
    print("#nombre:" ""+nombre+  "")
    print("#costo: S/. "+str(costo)+"")
    print("#descuento: S/. "+str(descuento)+"")
    print("############################")
