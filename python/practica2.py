"""
Programa practica2.py

Programa para calcular sueldo neto de un empleado dentro de una empresa:
    -Calcular el sueldo bruto mensual de un empleado de acuerdo con las siguientes indicaciones:
        -Cada empleado tiende un salario por horas laboradas
        
        -Si las horas trabajadas son:
            -Inferiores o iguales a 160:        Se paga el salario por hora indicado

            -Exceden las 160, sin pasar 200:    Las primeras 160 horas se pagan de acuerdo al salario indicado
                                                y las excedentes se pagan como extra a 1.5 del salario normal

            -Exceden las 200:                   Se aplica el criterio anterior y las horas excedentes de 200 
                                                se pagan como doble extra, siendo el doble del salario normal

    -Los impuestos a deducir se calcular con lo siguientes criterios:
        -Sueldo menos o igual a $4,000:         No paga impuesto

        -Hasta $20,000:                         Paga el 20% del excedente de $4,000

        -Hasta $30,000:                         Paga el impuesto anterior mas 25% del excedente de $20,000

        -Arriba de $30,00:                      Paga impuestos anteriores, mas 35% del excedente de $30,00

    -Seguridad social:
        -Todos los empleados                    Pagan 2.5% del sueldo bruto sin importar cantidad

    -Caja de ahorro de la empresa(Si es miembro):
        -Se le descuenta dependiendo del tipo de participacion:
            -Cuota fija:                        $1,000 mensuales

            -Cuota porcentual:                  3% o 5% (del sueldo bruto mensual)

    -Fondo de ahorro para el retiro, ahorro solidario(Si participa):
        -Cuotas:                                1% o 2% (del sueldo bruto mensual)

1. Constantes:
        impuesto_SS = 0.025


2. Datos de entrada:
    hrs_laboradas
    salario_hr
    participacion_ahorro
    participacion_retiro

3. Calculos:
    Para el salario:
        -Horas trabajadas inferiores o iguales a 160

            salario_brutoMensual = hrs_laboradas * salario_hr

        -Horas que exceden las 160, sin pasar 200

            hrs_extra         = (hrs_laboradas - 160) 

            salario_brutoMensual = (160 * salario_hr) + horas_extra * (salario_hr * 1.5) 

        -Horas que exceden las 200
            hrs_dobleExtra    = (hrs_laboradas - 200) 

            salario_brutoMensual = (160 * salario_hr) + 39 * (salario_hr 1.5) + horas_dobleExtra * (salario_hr * 2)
"""
