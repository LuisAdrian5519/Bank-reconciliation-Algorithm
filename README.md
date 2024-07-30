# Bank-Reconciliation-Algorithm
Discrepancy search Algorithm that seeks inconsistencies between Internal financial register and bank declaration.

PDF_Extraction: Script that extract the financial movements information (values, dates, and references) through each line of the PDF.

Excel_Extraction: Script that extract the financial movements information (values, dates, and references) accesing the columns in the financial movements table in Excel.

Main_TMI: Script the compares for each given value (financial movement) if this can be found in the other financial register. When inconsistencies are met, these movements are registered in a additional data strcture so later, they can be transformed into dataframes and displayed on a new Excel format automatically.

The inconsistencies displayed in Excel stand for:

- Incomes found in Bank declaration but not in Excel Auxiliar document
- Outcomes found in Bank declaration but not in Excel Auxiliar document
- Incomes found in Excel Auxiliar document but not in Bank declaration
- Outcomes found in Excel Auxiliar document but not in Bank declaration

Note: Due to confidentiality agreements with my employer, this repository does not include the documents it processes. 

