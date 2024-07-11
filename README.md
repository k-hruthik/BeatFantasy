# Converting Data from PDF to CSV and Inserting into MySQL Table

This guide explains how to convert data from a PDF file into a CSV file and then insert it into a MySQL table.

## Steps:

### 1. Extract Data from PDF

Use a Python script (`extractor.py`) to extract data from the PDF file (`user_teams.pdf`). Ensure Python and necessary libraries (like `pdfplumber`) are installed.

#### Python Script: `extractor.py`

```python
import pdfplumber
import csv

pdf_path = 'user_teams.pdf'
csv_path = 'output.csv'

with pdfplumber.open(pdf_path) as pdf:
    with open(csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    csvwriter.writerow(row)

print(f'Data extracted to {csv_path}')
