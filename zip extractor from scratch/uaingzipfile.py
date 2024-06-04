import zipfile
import os

def extract_zipfile(zip_path, extract_to):
    # Ensure the output directory exists
    os.makedirs(extract_to, exist_ok=True)
    
    # Open the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents into the specified directory
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to {extract_to}")


extract_zipfile('HISTDATA_COM_XLSX_EURUSD_M12018.zip', 'extracted')
