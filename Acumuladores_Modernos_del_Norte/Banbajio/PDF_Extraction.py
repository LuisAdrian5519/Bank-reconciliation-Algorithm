import PyPDF2

def Value_extraction():
   
   #         INSERT DATA HERE  :D
   
   
   
   Nombre_del_archivo_PDF = "TMI Banbajio Edo Cta Abril 2024.pdf"        # File
   Páginas_a_leer = 25                                                   # Number Pages
   Datos_a_ignorar_Inicio = 6                                            # Lines to ignore at the beggining of the document + 1
   Datos_a_ignorar_Final = 5                                             # Lines to ignore at the end of the document
   
   
   
   #        Beggining of algorithm
   
   
   # Variables declaration

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
   
   Beneficiarios = []
   Beneficiario_Ingresos = []
   Beneficiario_Egresos = []

   Movimiento = 0
   Fecha = 0
   Balance = 0
   i = 1

   # PDF Preprocessing - Opening and reading of PDF file

   PDF_File = open(Nombre_del_archivo_PDF, 'rb')
   PDF_reader = PyPDF2.PdfReader(PDF_File)

   Num_Pages = len(PDF_reader.pages)
   Max_Pages = min(Num_Pages, Páginas_a_leer)

   # PDF Processing - Partitioning, Reading, and Logging

   for Page in range(Max_Pages):
      
      Page_Object = PDF_reader.pages[Page]
      Text = Page_Object.extract_text()

      Lines = Text.split('\n')
   
      for idx, Line in enumerate(Lines):

         if '$' in Line:
         
            # Capture and Processing of Monetary Value, references, and beneficiary
            
            split_line = Line.split()
            dollar_index = split_line.index('$')
            elements_between = split_line[3:dollar_index]
            Reference = ' '.join(elements_between)
            
            Movimiento = Line.split('$')[1].strip() 
            Movimiento = float(Movimiento.replace(',', '').replace('-', ''))
            Movimientos.append(Movimiento)
            
            Fecha = Line.split()[0]
            Fechas.append(Fecha)
            
            Balance = Line.split()[-1]
            Balance = float(Balance.replace(',', ''))
            Balances.append(Balance)
            
            Referencias.append(Reference)

            Lines_count.append(Line)
            
            for i in range(1, 4):

               if idx + i < len(Lines):
               
                  next_line = Lines[idx + i]
                        
                  if 'BENEFICIARIO' in next_line or 'ORDENANTE' in next_line:
                     Beneficiarios.append(next_line)
                     break
                         
                  elif '$' in next_line:
                     Beneficiarios.append('N/A')
                     break


   # Post-Processing of Data Structures
   
   Movimientos = Movimientos[Datos_a_ignorar_Inicio:]
   Movimientos = Movimientos[:-Datos_a_ignorar_Final]

   Fechas = Fechas[Datos_a_ignorar_Inicio:]
   Fechas = Fechas[:-Datos_a_ignorar_Final]
   
   Balances = Balances[(Datos_a_ignorar_Inicio - 1):]
   Balances = Balances[:-Datos_a_ignorar_Final]
   
   Referencias = Referencias[Datos_a_ignorar_Inicio:]
   Referencias = Referencias[:-Datos_a_ignorar_Final]

   Beneficiarios = Beneficiarios[Datos_a_ignorar_Inicio:]
   Beneficiarios = Beneficiarios[:-Datos_a_ignorar_Final]

   Fechas = [int(char) for char in Fechas]
   
   for i in range(len(Movimientos)):
      
      if Balances[i + 1] < Balances[i]:
         
         Egresos.append(Movimientos[i])
         Fechas_Egresos.append(Fechas[i])
         Referencias_Egresos.append(Referencias[i])
         Beneficiario_Egresos.append(Beneficiarios[i])
         
      else: 
         
         Ingresos.append(Movimientos[i])
         Fechas_Ingresos.append(Fechas[i])
         Referencias_Ingresos.append(Referencias[i])
         Beneficiario_Ingresos.append(Beneficiarios[i])
         
   Balance_Line = Lines_count[3]

   Balance_values = Balance_Line.split('$')[1:] 
   Balance_values = [value.strip() for value in Balance_values]

   Ingreso_Total = float(Balance_values[1].replace(',', ''))
   Egreso_Total = float(Balance_values[2].replace(',', ''))
         
   return Ingresos, Egresos, Fechas_Ingresos, Fechas_Egresos, Ingreso_Total, Egreso_Total, Referencias_Ingresos, Referencias_Egresos, Beneficiario_Ingresos, Beneficiario_Egresos


Ingresos, Egresos, Fechas_Ingresos, Fechas_Egresos, Ingreso_Total, Egreso_Total, Referencias_Ingresos, Referencias_Egresos, Beneficiario_Ingresos, Beneficiario_Egresos = Value_extraction()

