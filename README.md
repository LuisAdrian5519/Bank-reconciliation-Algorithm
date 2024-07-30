# Bank-Reconciliation-Algorithm
Discrepancy search Algorithm that seeks inconsistencies between Internal financial register and bank declaration.

PDF_Extraction: Script that extract the financial movements information (values, dates, and references) through each line of the PDF.

Excel_Extraction: Script that extract the financial movements information (values, dates, and references) accesing the columns in the financial movements table in Excel.

Main_TMI: Script the compares for each given value (financial movement) if this can be found in the other financial register. When inconsistencies are met, these movements are registered in a additional data strcture so later, they can be transformed into dataframes and displayed on a new Excel format.
