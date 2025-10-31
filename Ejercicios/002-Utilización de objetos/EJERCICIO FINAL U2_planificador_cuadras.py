'''
Calcular numero cuadras en una fecha dada
Numero cuadras segun numero de caballos y capacidad de la cuadra
Redondear al alza el número de cuadras (math.ceil)
Mostrar propiedades fecha (datetime.date, date.year, date.weekday)
Mostras por pantalla informe

'''
import math as mates
import datetime

#Pido los datos para los calculos de cuadras
caballos = int(input("Dime cuantos caballos quieres meter en cuadras: "))
capacidad_por_cuadra = int(input("Dime cuantos caballos iran en cada cuadra: "))

#Pido los datos para la fecha:
ano =  int(input("Dime el año: "))
mes =  int(input("Dime el mes: "))
dia =  int(input("Dime el dia: "))

#Calculo las cuadras que necesito por caballos

cuadras = mates.ceil(caballos/capacidad_por_cuadra)


try:
    
    fecha = datetime.date(ano, mes, dia)

    # Día de la semana con weekday() y isoweekday()
    numero_weekday = fecha.weekday()       # 0 = lunes, 6 = domingo
    numero_isoweekday = fecha.isoweekday() # 1 = lunes, 7 = domingo
    nombre_dia = fecha.strftime("%A")      # Ejemplo: "lunes"


    # Determinar si es entre semana o fin de semana
    dia_semana = fecha.isoweekday()
    if dia_semana <= 5:
        tipo_dia = "Entre semana"
    else:
        tipo_dia = "Fin de semana"

    #Informe
    print("##############################################################################")
    print(" INFORME:")
    print("----------------------------------------------------------------")
    print("Fecha: ", fecha)
    print("Año: ", ano)
    print("Mes: ", mes)
    print("Día: ", dia)
    print("Día de la semana: ", nombre_dia)
    print("Weekday: ", numero_weekday)
    print("Isoweekday: ", numero_isoweekday)
    print("La fecha cae en:", tipo_dia)
    print("----------------------------------------------------------------")
    print("Numero de caballos que quiero meter en cuadras: ",caballos)
    print("Numero de caballos que caben por cuadra: ",capacidad_por_cuadra)
    print("Numero de cuadras que necesito para meter a los caballos: ",cuadras)
    print("##############################################################################")
except:
    print("No he podido relizar la fecha, por lo que no puedo sacar el Informe")




