import PyPDF2

def Value_extraction():
   
   #         INSERTAR DATOS AQUÍ  :D
   
   
   
   Nombre_del_archivo_PDF = "TMI Banbajio Edo Cta Marzo 2024.pdf"        # Nombre del Archivo
   Páginas_a_leer = 15                                                     # Número de Páginas a leer
   Datos_a_ignorar_Inicio = 6                                              # Filas a ignorar al inicio del documento
   Datos_a_ignorar_Final = 0                                               # Filas a ignorar al Final del documento
   
   
   
   #        INICIO DEL CÓDIGO
   
   
   # Declaración de variables

   Movimientos = []
   Ingresos = []
   Egresos = []
   
   Fechas = []
   Fechas_Ingresos = []
   Fechas_Egresos = []
   
   Balances = []
   Lines_count =[]
   Balance_values = []
   
   Referencias = []
   Referencias_Ingresos = []
   Referencias_Egresos = []

   Movimiento = 0
   Fecha = 0
   Balance = 0
   i = 1

   # Preprocesamiento del archivo PDF - Apertura y lectura

   PDF_File = open(Nombre_del_archivo_PDF, 'rb')
   PDF_reader = PyPDF2.PdfReader(PDF_File)

   Num_Pages = len(PDF_reader.pages)
   Max_Pages = min(Num_Pages, Páginas_a_leer)

   # Procesamiento del archivo PDF - Partición, lectura y registro

   for Page in range(Max_Pages):
      
      Page_Object = PDF_reader.pages[Page]
      Text = Page_Object.extract_text()

      Lines = Text.split('\n')
   
      for Line in Lines:

         if '$' in Line:
         
            # Captura y procesamiento del valor monetario después del símbolo "$"
            
            split_line = Line.split()
            dollar_index = split_line.index('$')
            elements_between = split_line[3:dollar_index]
            Reference = ' '.join(elements_between)
            
            Movimiento = Line.split('$')[1].strip() 
            Movimiento = float(Movimiento.replace(',', ''))
            Movimientos.append(Movimiento)
            
            Fecha = Line.split()[0]
            Fechas.append(Fecha)
            
            Balance = Line.split()[-1]
            Balance = float(Balance.replace(',', ''))
            Balances.append(Balance)
            
            Referencias.append(Reference)

            Lines_count.append(Line)


   # Postprocesamiento de las estructuras de datos
   
   Movimientos = Movimientos[Datos_a_ignorar_Inicio:]
   Movimientos = Movimientos[:-Datos_a_ignorar_Final]

   Fechas = Fechas[Datos_a_ignorar_Inicio:]
   Fechas = Fechas[:-Datos_a_ignorar_Final]
   
   Balances = Balances[(Datos_a_ignorar_Inicio - 1):]
   Balances = Balances[:-Datos_a_ignorar_Final]
   
   Referencias = Referencias[Datos_a_ignorar_Inicio:]
   Referencias = Referencias[:-Datos_a_ignorar_Final]

   Fechas = [int(char) for char in Fechas]
   
   for i in range(len(Movimientos)):
      
      if Balances[i + 1] < Balances[i]:
         
         Egresos.append(Movimientos[i])
         Fechas_Egresos.append(Fechas[i])
         Referencias_Egresos.append(Referencias[i])
         
      else: 
         
         Ingresos.append(Movimientos[i])
         Fechas_Ingresos.append(Fechas[i])
         Referencias_Ingresos.append(Referencias[i])
         
   Balance_Line = Lines_count[3]

   Balance_values = Balance_Line.split('$')[1:] 
   Balance_values = [value.strip() for value in Balance_values]

   Ingreso_Total = float(Balance_values[1].replace(',', ''))
   Egreso_Total = float(Balance_values[2].replace(',', ''))
         
   return Ingresos, Egresos, Fechas_Ingresos, Fechas_Egresos, Ingreso_Total, Egreso_Total, Referencias_Ingresos, Referencias_Egresos

# Dev Diagnosis

Lista_de_valores_MNA_BBVA_Ingresos, Lista_de_valores_MNA_BBVA_Egresos, Lista_de_valores_MNA_BBVA_Fechas_Ingresos, Lista_de_valores_MNA_BBVA_Fechas_Egresos, Ingreso_Total, Egreso_Total, Referencias_Ingresos, Referencias_Egresos = Value_extraction()

print(Lista_de_valores_MNA_BBVA_Ingresos)
print("---------------------------------------------------")
print(Lista_de_valores_MNA_BBVA_Egresos)
print("---------------------------------------------------")
print(Lista_de_valores_MNA_BBVA_Fechas_Ingresos)
print("---------------------------------------------------")
print(Lista_de_valores_MNA_BBVA_Fechas_Egresos)
print("---------------------------------------------------")
print(Ingreso_Total)
print("---------------------------------------------------")
print(Egreso_Total)
print("---------------------------------------------------")
print(Referencias_Ingresos)
print("---------------------------------------------------")
print(Referencias_Egresos)
print("---------------------------------------------------")


