# Importar Librerías externas 

import pandas as pd
import openpyxl

# Importar módulos propios

import PDF_Extraction as PDF
import Excel_Extraction as Excel

# Data Set-up

Lista_de_valores_MNA_BBVA_Ingresos, Lista_de_valores_MNA_BBVA_Egresos, Lista_de_valores_MNA_BBVA_Fechas_Ingresos, Lista_de_valores_MNA_BBVA_Fechas_Egresos, Ingreso_Total, Egreso_Total, Referencias_MNA_BBVA_Ingresos, Referencias_MNA_BBVA_Egresos = PDF.Value_extraction()
Lista_de_valores_Auxiliar_Ingresos, Lista_de_valores_Auxiliar_Egresos, Lista_de_valores_Auxiliar_Fechas_Ingresos, Lista_de_valores_Auxiliar_Fechas_Egresos, Referencias_Auxiliar_Ingresos, Referencias_Auxiliar_Egresos = Excel.Value_extraction()

print("")
print("            Comparador de Dineros")
print("")

# Revisión de coincidencia entre Ingresos y Egresos registrados y declarados por el Banco

print("")
print("Antes de comenzar...")
print("")

Suma_Ingresos_MNA_BBVA = sum(Lista_de_valores_MNA_BBVA_Ingresos)
Suma_Egresos_MNA_BBVA = sum(Lista_de_valores_MNA_BBVA_Egresos)

print(f"\033[1m                    Banco  |  Base de datos Capturada \033[0m ")
print("")
print(f"Ingresos:     {Ingreso_Total}  -  {Suma_Ingresos_MNA_BBVA}  ")
print("")
print(f"Diferencia:              {Ingreso_Total - Suma_Ingresos_MNA_BBVA}")
print("---------------------------------------------------------")
print("")
print(f"Egresos:     {Egreso_Total}  -  {Suma_Egresos_MNA_BBVA}  ")
print("")
print(f"Diferencia:              {Egreso_Total - Suma_Egresos_MNA_BBVA}")
print("---------------------------------------------------------")
print("")

# Declaración de variables

#    Ingresos MNA BBVA
Ingresos_en_ambas_listas_MNA_BBVA = []
Fechas_en_ambas_listas_Ingresos_MNA_BBVA = []
Valores_en_ninguna_lista_MNA_BBVA_Ingresos = []
Fechas_en_ninguna_lista_Ingresos_MNA_BBVA = []

#    Ingresos Auxiliar
Ingresos_en_ambas_listas_auxiliar = []
Fechas_en_ambas_listas_Ingresos_auxiliar = []
Valores_en_ninguna_lista_auxiliar_Ingresos = []
Fechas_en_ninguna_lista_Ingresos_auxiliar = []

#    Egresos MNA BBVA
Egresos_en_ambas_listas_MNA_BBVA = []
Fechas_en_ambas_listas_Egresos_MNA_BBVA = []
Valores_en_ninguna_lista_MNA_BBVA_Egresos = []
Fechas_en_ninguna_lista_Egresos_MNA_BBVA = []

#    Egresos Auxiliar
Egresos_en_ambas_listas_auxiliar = []
Fechas_en_ambas_listas_Egresos_auxiliar = []
Valores_en_ninguna_lista_auxiliar_Egresos = []
Fechas_en_ninguna_lista_Egresos_auxiliar = []

#    Variables Auxiliares

Lista_de_valores_Auxiliar_Ingresos_Copia = Lista_de_valores_Auxiliar_Ingresos.copy()
Lista_de_valores_Auxiliar_Egresos_Copia = Lista_de_valores_Auxiliar_Egresos.copy()


# Funciones para Márgenes de Error y definición del mes

mes = "Ene"  
Margen_de_error = 1   # Margen de error de un peso
Margen_de_error_temp = 3   # Margen de error de 3 días

def fechas_dentro_del_margen(fecha1, fecha2, margen):
    return abs(fecha1 - fecha2) <= margen or abs(fecha1 - fecha2) == 0 

def valores_dentro_del_margen(valor1, valor2, margen):
    return abs(valor1 - valor2) <= margen

# Función para comparación entre Listas

def Comparador(Lista_de_valores_Banco, Lista_de_Fechas_Banco, Lista_de_valores_Auxiliar, Lista_de_Fechas_Auxiliar, Valores_en_ambas_listas, Fechas_en_ambas_listas, Valores_en_ninguna_lista, Fechas_en_ninguna_lista, Referencias):

   for i, A in enumerate(Lista_de_valores_Banco):
    
       fecha_A = Lista_de_Fechas_Banco[i]
       Found = False

       for j, B in enumerate(Lista_de_valores_Auxiliar):
       
          fecha_B = Lista_de_Fechas_Auxiliar[j]

          if fechas_dentro_del_margen(fecha_A, fecha_B, Margen_de_error_temp) and valores_dentro_del_margen(A, B, Margen_de_error) and (A not in Valores_en_ambas_listas or Lista_de_Fechas_Banco[i] not in Fechas_en_ambas_listas or Lista_de_valores_Banco.count(A) > 1):

               Valores_en_ambas_listas.append(A)
               Fechas_en_ambas_listas.append(fecha_A)
               Found = True
               print(f"\033[1mConsistente     Banco  |  Auxiliar \033[0m ")
               print(f"Cantidad:     {A}  -  {B}  ")
               print(f"Fecha:      {fecha_A} {mes}   -   {fecha_B} {mes}")
               print("")
               Lista_de_valores_Auxiliar[j] = 0
               Referencias[i] = "0"
               break

       if not Found:

           Valores_en_ninguna_lista.append(A)
           Fechas_en_ninguna_lista.append(fecha_A)
           print(f"\033[1mInconsistente:\033[0m {A}")
           print(f"Fecha: {Lista_de_Fechas_Banco[i]} {mes}")
           print("")
           
   print("")
   print("-------------------------------------------------------------------------------------------------")
   print("")
        
   return Valores_en_ambas_listas, Fechas_en_ambas_listas, Valores_en_ninguna_lista, Fechas_en_ninguna_lista

# Ciclo de Trabajo 1: Ingresos registrados en el banco, pero no en Excel
Comparador(Lista_de_valores_MNA_BBVA_Ingresos, Lista_de_valores_MNA_BBVA_Fechas_Ingresos, Lista_de_valores_Auxiliar_Ingresos_Copia, Lista_de_valores_Auxiliar_Fechas_Ingresos, Ingresos_en_ambas_listas_MNA_BBVA, Fechas_en_ambas_listas_Ingresos_MNA_BBVA, Valores_en_ninguna_lista_MNA_BBVA_Ingresos, Fechas_en_ninguna_lista_Ingresos_MNA_BBVA, Referencias_MNA_BBVA_Ingresos)

# Ciclo de Trabajo 2: Egresos registrados en el banco, pero no en Excel
Comparador(Lista_de_valores_MNA_BBVA_Egresos, Lista_de_valores_MNA_BBVA_Fechas_Egresos, Lista_de_valores_Auxiliar_Egresos_Copia, Lista_de_valores_Auxiliar_Fechas_Egresos, Egresos_en_ambas_listas_MNA_BBVA, Fechas_en_ambas_listas_Egresos_MNA_BBVA, Valores_en_ninguna_lista_MNA_BBVA_Egresos, Fechas_en_ninguna_lista_Egresos_MNA_BBVA, Referencias_MNA_BBVA_Egresos)

# Ciclo de Trabajo 3: Ingresos registrados en Excel, pero no en el banco
Comparador(Lista_de_valores_Auxiliar_Ingresos, Lista_de_valores_Auxiliar_Fechas_Ingresos, Lista_de_valores_MNA_BBVA_Ingresos, Lista_de_valores_MNA_BBVA_Fechas_Ingresos, Ingresos_en_ambas_listas_auxiliar, Fechas_en_ambas_listas_Ingresos_auxiliar, Valores_en_ninguna_lista_auxiliar_Ingresos, Fechas_en_ninguna_lista_Ingresos_auxiliar, Referencias_Auxiliar_Ingresos)

# Ciclo de Trabajo 4: Egresos registrados en Excel, pero no en el banco
Comparador(Lista_de_valores_Auxiliar_Egresos, Lista_de_valores_Auxiliar_Fechas_Egresos, Lista_de_valores_MNA_BBVA_Egresos, Lista_de_valores_MNA_BBVA_Fechas_Egresos, Egresos_en_ambas_listas_auxiliar, Fechas_en_ambas_listas_Egresos_auxiliar, Valores_en_ninguna_lista_auxiliar_Egresos, Fechas_en_ninguna_lista_Egresos_auxiliar, Referencias_Auxiliar_Egresos)

Referencias_MNA_BBVA_Ingresos = [x for x in Referencias_MNA_BBVA_Ingresos if x != "0"]
Referencias_MNA_BBVA_Egresos = [x for x in Referencias_MNA_BBVA_Egresos if x != "0"]
Referencias_Auxiliar_Ingresos = [x for x in Referencias_Auxiliar_Ingresos if x != "0"]
Referencias_Auxiliar_Egresos = [x for x in Referencias_Auxiliar_Egresos if x != "0"]

# Dataframe en Pandas y Exportación a Excel

#    Ingresos MNA BBVA
Inconsistencias_Ingresos_MNA_BBVA = {
    'Fechas': Fechas_en_ninguna_lista_Ingresos_MNA_BBVA,
    'Valores': Valores_en_ninguna_lista_MNA_BBVA_Ingresos,
    'Referencias': Referencias_MNA_BBVA_Ingresos}

#    Egresos MNA BBVA
Inconsistencias_Egresos_MNA_BBVA = {
    'Fechas': Fechas_en_ninguna_lista_Egresos_MNA_BBVA,
    'Valores': Valores_en_ninguna_lista_MNA_BBVA_Egresos,
    'Referencias': Referencias_MNA_BBVA_Egresos}

#    Ingresos Auxiliar
Inconsistencias_Ingresos_Auxiliar = {
    'Fechas': Fechas_en_ninguna_lista_Ingresos_auxiliar,
    'Valores': Valores_en_ninguna_lista_auxiliar_Ingresos,
    'Referencias': Referencias_Auxiliar_Ingresos}

#    Egresos Auxiliar
Inconsistencias_Egresos_Auxiliar = {
    'Fechas': Fechas_en_ninguna_lista_Egresos_auxiliar,
    'Valores': Valores_en_ninguna_lista_auxiliar_Egresos,
    'Referencias': Referencias_Auxiliar_Egresos}

#   Generación de Dataframes

Tabla_Inconsistencias_Ingresos_MNA_BBVA = pd.DataFrame(Inconsistencias_Ingresos_MNA_BBVA)
Tabla_Inconsistencias_Egresos_MNA_BBVA = pd.DataFrame(Inconsistencias_Egresos_MNA_BBVA)
Tabla_Inconsistencias_Ingresos_Auxiliar = pd.DataFrame(Inconsistencias_Ingresos_Auxiliar)
Tabla_Inconsistencias_Egresos_Auxiliar = pd.DataFrame(Inconsistencias_Egresos_Auxiliar)

#   Concatenación con encabezado

general_header_ingresos_banco = pd.DataFrame([["Ingresos registrados en Banco y no en Auxiliar", "", ""]],
                                             columns = ['Fechas', 'Valores', 'Referencias'])
general_header_egresos_banco = pd.DataFrame([["Egresos registrados en Banco y no en Auxiliar", "", ""]],
                                             columns = ['Fechas', 'Valores', 'Referencias'])
general_header_ingresos_auxiliar = pd.DataFrame([["Ingresos registrados en Auxiliar y no en Banco", "", ""]],
                                             columns = ['Fechas', 'Valores', 'Referencias'])
general_header_egresos_auxiliar = pd.DataFrame([["Egresos registrados en Auxiliar y no en Banco", "", ""]],
                                             columns = ['Fechas', 'Valores', 'Referencias'])

Tabla_Inconsistencias_Ingresos_MNA_BBVA = pd.concat([general_header_ingresos_banco, Tabla_Inconsistencias_Ingresos_MNA_BBVA], ignore_index=True)
Tabla_Inconsistencias_Egresos_MNA_BBVA = pd.concat([general_header_egresos_banco, Tabla_Inconsistencias_Egresos_MNA_BBVA], ignore_index=True)
Tabla_Inconsistencias_Ingresos_Auxiliar = pd.concat([general_header_ingresos_auxiliar, Tabla_Inconsistencias_Ingresos_Auxiliar], ignore_index=True)
Tabla_Inconsistencias_Egresos_Auxiliar = pd.concat([general_header_egresos_auxiliar, Tabla_Inconsistencias_Egresos_Auxiliar], ignore_index=True)

#   Conversión a archivo Excel

with pd.ExcelWriter('Inconsistencias.xlsx') as writer:
    Tabla_Inconsistencias_Ingresos_MNA_BBVA.to_excel(writer, sheet_name = 'Ingresos Banco', index = False, header = True)
    Tabla_Inconsistencias_Egresos_MNA_BBVA.to_excel(writer, sheet_name = 'Egresos Banco', index = False, header = True)
    Tabla_Inconsistencias_Ingresos_Auxiliar.to_excel(writer, sheet_name = 'Ingresos Auxiliar', index = False, header = True)
    Tabla_Inconsistencias_Egresos_Auxiliar.to_excel(writer, sheet_name = 'Egresos Auxiliar', index = False, header = True)

print("")
print("Archivo Excel exportado con éxito")
print("")
print("")