"""
Programa calculadora_ISR.py
Autor: Ivan Javier Gordillo Solis

1. Tasa de impuestos, deduccion estandar y deduccion por dependiente/s descritas para todos los contribuyentes, de acuerdo con las leyes fiscales:
    La tasa de impuestos de 20% es fija
        tasa_impuestos = 0.2

    Se permite una deduccion estandar de: $10,000.00 pesos
        deduccion_estandar = 10000

    Por cada dependiente, se permite una deduccion adicional de: $2,000.00
        deduccion_dependientes = 2000

2. Datos de entrada:
    -Sueldo bruto (Al centavo mas cercano)

    -Número de dependientes

3. Calculos necesarios para obtener ISR

    -Deduccion correspondiente al numero de dependientes
        Numero de dependientes * $2,000

    -Impuesto preliminar con la deduccion estandar, sin deduccion de dependientes
        [sueldo bruto - deduccion estandar] * tasa de impuestos (En forma decimal)

    -ISR a pagar 
        impuesto preliminar - deduccion adicional

4. Los datos de salida son:
    -El total a pagar de ISR anual
"""

#Inicializacion de constantes(Tasa de impuestos, Valor de deduccion: estandar y por cada dependiente).
tasa_impuestos = 0.2
deduccion_estandar = 10000
deduccion_dependientes = 2000

#Se piden ingresar los datos de entrada con anotaciones para evitar error alguno
print(" ~Calculo de ISR anual~ \n")
print("A continuacion ingrese el sueldo bruto anual del contribuyente y numero de dependientes \nNota. No deben de agregarse espacios\n      Y de no existir dependientes, escribir: 0 \n")
sueldo_bruto = float(input("Sueldo bruto anual (Con centavos): $"))
dependientes = int((input("Numero de dependientes: ")))

#Obtencion de deducciones por personas dependientes
deduccion_adicional = dependientes * deduccion_dependientes

#Obtencion de impuestos sin deduccion adicional, primero restando lo correspondiente de la deduccion estandar 
impuesto_preliminar = (sueldo_bruto - deduccion_estandar) * tasa_impuestos

#Obtencion final de impuestos a pagar, reduciendo lo correspondiente por deduccion de dependientes y redondeando a centavos
impuesto_final = round((impuesto_preliminar - deduccion_adicional), 2)

#Se despliega el total a pagar de ISR del contribuyente
print()
print("El total a pagar de Impuesto Sobre la Renta (ISR) es de: $" + str(impuesto_final) + "\n\n~Ivan Javier Gordillo Solis \n~2223028708")