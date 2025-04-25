-- SQL queries for data extraction and validation purposes

-- Query to select all records from a specific table
SELECT * FROM your_table_name;

-- Query to count the number of records in a table
SELECT COUNT(*) FROM your_table_name;

-- Query to find missing values in a specific column
SELECT COUNT(*) FROM your_table_name WHERE your_column_name IS NULL;

-- Query to validate data types in a specific column
SELECT your_column_name, DATA_TYPE 
FROM information_schema.columns 
WHERE table_name = 'your_table_name';

-- Query to get distinct values in a column
SELECT DISTINCT your_column_name FROM your_table_name;

-- Query to check for duplicates in a specific column
SELECT your_column_name, COUNT(*) 
FROM your_table_name 
GROUP BY your_column_name 
HAVING COUNT(*) > 1;