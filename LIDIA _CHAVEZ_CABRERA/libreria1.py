#01
#si el tipo de servicio de colectivos son buenos
#aqui una funcion upper
def descuento (tipo,prestamo):
    if (tipo.upper()== "BUENO"):
        return 0.20 * prestamo
    else:
        return 0
def reporte_prestamo(nombre,precio,descuento):
    print("############################")
    print("#reporte de prestamo#")
    print("#nombre:" ""+nombre+  "")
    print("#precio: S/. "+str(precio)+"")
    print("#descuento: S/. "+str(descuento)+"")
    print("############################")

