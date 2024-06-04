import zipfile
import xml.etree.ElementTree as ET
from zip_extractor import extract_zip



# Extract the XLSX file using zipfile
with zipfile.ZipFile('extracted/DAT_XLSX_EURUSD_M1_2018.xlsx', 'r') as xlsx_zip:
    xlsx_zip.extractall('extracted_xlsx')

# Parse the XML file from the extracted XLSX content
tree = ET.parse('extracted_xlsx/xl/worksheets/sheet1.xml')
root = tree.getroot()

# Iterate over the rows and cells
i = 0
for row in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
    print('')
    if i >= 10:
        break
    for cell in row.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
        value = cell.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
        if value is not None:
            print(value.text, end='/')
    i += 1
