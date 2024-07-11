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
### 2. Create MySQL Database Table

Create a MySQL database table named `user_teams` with appropriate columns to store the extracted data.

#### Example `CREATE TABLE` SQL Statement

```sql
CREATE TABLE user_teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 VARCHAR(255),
    column3 VARCHAR(255),
    column4 VARCHAR(255),
    column5 VARCHAR(255),
    column6 VARCHAR(255),
    column7 VARCHAR(255),
    column8 VARCHAR(255),
    column9 VARCHAR(255),
    column10 VARCHAR(255),
    column11 VARCHAR(255)
);

