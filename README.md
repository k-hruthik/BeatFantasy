# Conversion of user_teams.pdf to Database Table

This project involves extracting data from `user_teams.pdf`, creating a database table named `user_teams`, and inserting the extracted data into this table.

## Steps:

### 1. Extract Data from user_teams.pdf

Use `extractor.py` to extract data from `user_teams.pdf`. Ensure Python and necessary libraries (like `pdfplumber`) are installed and configured.

```bash
python extractor.py
# Conversion of user_teams.pdf to Database Table

This project involves extracting data from `user_teams.pdf`, creating a database table named `user_teams`, and inserting the extracted data into this table.

## Steps:

### 2. Create Database Table

Create a MySQL database table named `user_teams` with appropriate columns to store the extracted data. Here's an example `CREATE TABLE` SQL statement:

```sql
CREATE TABLE user_teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 VARCHAR(255),
    ...  -- Define columns based on extracted data structure
);
