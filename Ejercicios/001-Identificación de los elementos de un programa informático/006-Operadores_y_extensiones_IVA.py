base_imponible = 0
total_iva = 0
total_factura = 0

base_imponible = float(input("Introduce la base imponible de la factura: "))

total_iva = base_imponible * 0.21
total_factura = base_imponible + total_iva

print("Base imponible:",base_imponible)
print("IVA (21%)",total_iva)
print("Total de la factura: ",total_factura)