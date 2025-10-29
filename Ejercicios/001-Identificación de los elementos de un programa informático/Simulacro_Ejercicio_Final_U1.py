'''
---------------------------------
Programa: Tiket Tienda
version: 1.0
Autora: Ruth Sainz
Año: 2025
---------------------------------
'''


IVA = 0.21
cliente_nombre = input("Introduzca su nombre: ") # Pido al cliente  que me diga su nombre
edad = int(input("Introduce tu edad: ")) # Le pido su edad 

if edad < 18: #Me aseguro de que es mayor de edad
    print(" No puedo darte la factura porque eres menor")
else:
    base_imponible = float(input("Introduce la base imponible de la factura: ")) # Le pido la base imponible sobre la que haré los cálculos
    if base_imponible >= 0: #Me aseguro de que sea un número positivo
        if base_imponible < 100:

            #Se le aplica un 0% de descuento
            print("0% de descuento")

            importe_descuento = base_imponible * 0
            base_tras_descuento = base_imponible - importe_descuento
            importe_iva = base_tras_descuento * IVA
            total_factura = base_tras_descuento + importe_iva

            print(total_factura)

        elif base_imponible >= 100 and base_imponible <= 199.99:

            #Se le aplica un 5% de descuento
            print("5% de descuento")

            importe_descuento = base_imponible * 0.05
            base_tras_descuento = base_imponible - importe_descuento
            importe_iva = base_tras_descuento * IVA
            total_factura = base_tras_descuento + importe_iva

            print(total_factura)


        elif base_imponible  >= 200:

            #Se le aplica un 10% de descuento
            print("10% de descuento")

            importe_descuento = base_imponible * 0.10
            base_tras_descuento = base_imponible - importe_descuento
            importe_iva = base_tras_descuento * IVA
            total_factura = base_tras_descuento + importe_iva
            
            print(total_factura)
    else:  #Si no es un número positivo le digo al cliente que no puedo realizar ningún cálculo
        print("Con estos números no puedo sacarte nada")
