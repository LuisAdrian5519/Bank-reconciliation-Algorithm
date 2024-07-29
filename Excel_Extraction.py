import openpyxl
from tabulate import tabulate

def Value_extraction():

   #         INSERTAR DATOS AQUÍ  :D
   
   
   
   Nombre_del_archivo_Excel = "Conciliación Banbajio Cta.01 Marzo 2024.xlsx"          # Nombre del Archivo
   Columna_para_fechas = 0                                                            # Columna de Excel en la cual se encuentran las fechas 
   Columna_para_ingresos = 3                                                          # Columna de Excel en la cual se encuentran los ingresos
   Columna_para_egresos = 4                                                           # Columna de Excel en la cual se encuentran los Egresos
   Columna_para_referencias = 2
   
   
   
   #        INICIO DEL CÓDIGO
   
   
   # Declaración de variables

   Ingresos = []
   Ingresos_aux = []
   
   Egresos = []
   
   Fechas = []
   Fechas_Ingresos = []
   Fechas_Egresos = []
   
   Referencias_General_Auxiliar1 = []
   Referencias_General_Auxiliar2 = []
   Referencias_Ingresos = []
   Referencias_Egresos = []

   # Preprocesamiento del archivo PDF - Apertura y lectura

   Excel = openpyxl.load_workbook(Nombre_del_archivo_Excel)
   Dataframe = Excel.active

   # Procesamiento del archivo Excel - Lectura y registro

   for row in Dataframe.iter_rows(2, Dataframe.max_row - 1):
        
       Fechas.append(row[Columna_para_fechas].value)
       Ingresos.append(row[Columna_para_ingresos].value)
       Ingresos_aux.append(row[Columna_para_ingresos].value)
       Egresos.append(row[Columna_para_egresos].value)
       Referencias_General_Auxiliar1.append(row[Columna_para_referencias].value)
       Referencias_General_Auxiliar2.append(row[Columna_para_referencias].value)
       
       

   Dias = [Fecha.day for Fecha in Fechas if Fecha is not None]
   
   Ingresos = [valor for valor in Ingresos if valor != 0]
   Egresos = [valor for valor in Egresos if valor != 0]
   
   Ingresos = Ingresos[:-5]
   Ingresos_aux = Ingresos_aux[:-5]
   Egresos = Egresos[:-5]
   
   # POst-Procesamiento del archivo Excel - Separación en Ingresos y Egresos
   
   for i in range(len(Ingresos_aux)):
       
       if Ingresos_aux[i] == 0:
       
           Fechas_Egresos.append(Dias[i])
           Referencias_Egresos.append(Referencias_General_Auxiliar2[i])
           
       else:
           
           Fechas_Ingresos.append(Dias[i])
           Referencias_Ingresos.append(Referencias_General_Auxiliar1[i])
    
   return Ingresos, Egresos, Fechas_Ingresos, Fechas_Egresos, Referencias_Ingresos, Referencias_Egresos

# Dev Diagnosis

# Lista_de_valores_Auxiliar_Ingresos, Lista_de_valores_Auxiliar_Egresos, Lista_de_valores_Auxiliar_Fechas_Ingresos, Lista_de_valores_Auxiliar_Fechas_Egresos, Referencias_Ingresos, Referencias_Egresos  = Value_extraction()

# print(Lista_de_valores_Auxiliar_Ingresos)
# print("---------------------------------------------------")
# print(Lista_de_valores_Auxiliar_Egresos)
# print("---------------------------------------------------")
# print(Lista_de_valores_Auxiliar_Fechas_Ingresos)
# print("---------------------------------------------------")
# print(Lista_de_valores_Auxiliar_Fechas_Egresos)
# print("---------------------------------------------------")
# print(Referencias_Ingresos)
# print("---------------------------------------------------")
# print(Referencias_Egresos)
# print("---------------------------------------------------")










