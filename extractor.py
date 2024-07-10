import pdfplumber
import pandas as pd

# Function to extract and process text from PDF
def extract_pdf_data(file_path):
    with pdfplumber.open(file_path) as pdf:
        pages = pdf.pages
        data = []
        for page in pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                if line.strip():  # Skip empty lines
                    # Process each line into a list, filling missing values with None
                    elements = [elem.strip() if elem.strip() else None for elem in line.split(' ')]
                    # Ensure each row has exactly 12 columns
                    elements = elements + [None] * (12 - len(elements)) if len(elements) < 12 else elements[:12]
                    data.append(elements)
    return data

# Path to your PDF file
pdf_file_path = 'C:/Users/hruth/Downloads/user_teams.pdf'

# Extract data from PDF
data = extract_pdf_data(pdf_file_path)

# Convert to DataFrame
columns = ['user_team', 'player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11']
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)

# Save DataFrame to CSV (optional)
df.to_csv('output.csv', index=False)
