'''
----------------------------------------
Programa: Factura con IVA y Descuento
Versión: 1.0
Autora: Ruth Sainz
Año: 2025
Descripción: Programa que calcule el total de una factura aplicando IVA y un descuento fijo de 10€ solo si el precio bruto es igual o mallor a 50€.
----------------------------------------
'''

IVA = 0.21
DESCUENTO = 10

#Primero le pedimos al cliente que introduzca su nombre y el precio bruto de su compra.

nombre_cliente = input("Introduzca su nombre: ") 
precio_bruto = float(input("Introduzca el precio bruto de la compra: "))

#Miro que la compra sea mayor o igual a 50€ para ver si aplico el descuento o no.

if precio_bruto >= 50:
 #Aplico el IVA al precio bruto
 iva_aplicado = precio_bruto * IVA
 subtotal_con_iva = precio_bruto + iva_aplicado

 #Creo una variable descuento aparte para poder mostrar en el resumen final que si se aplica el descuento.
 descuento = 10

 #Aplico el decsuento de 10€
 total_a_pagar = subtotal_con_iva - DESCUENTO

else: 
 #Aplico el IVA al precio bruto
 iva_aplicado = precio_bruto * IVA
 subtotal_con_iva = precio_bruto + iva_aplicado
 #Creo una variable descuento aparte para poder mostrar en el resumen final que no se aplica el descuento.
 descuento = 0

 #Doy el precio de la factura sin descuento
 total_a_pagar = subtotal_con_iva

#Le muetsro al cliente sus datos, un resumen y el total de su factura.

print("------------------------")
print("Nombre Cliente: ",nombre_cliente)
print("Precio Bruto: ",precio_bruto)
print("IVA aplicado: ", iva_aplicado)
print("Descuento: ",descuento)
print("TOTAL A PAGAR: ", total_a_pagar)
print("------------------------")
