import pandas as pd
import sqlite3

# Step 1 : Create a connection to SQLite Database
conn = sqlite3.connect ('healthcare.db')

# Step 2 : Create a Pandas DataFrame
df = pd.read_csv('https://healthdata.gov/resource/xn3e-yyaj.csv')
print(df)

# Print column names
print("Column Names:")
print(df.columns)

# Save the DataFrame to the SQLite database
df.to_sql('healthcare_data', conn, if_exists='replace', index=False)

# Step 3: Perform SQL Queries Using SQLite and Pandas

# Query 0: Convert age group columns into age categories
query_age_groups = pd.read_sql_query("""
    SELECT state,
           SUM(_1) AS "Victims < 1",
           SUM(_2) AS "Victims Age 1",
           SUM(_3) AS "Victims Age 2",
           SUM(_4) AS "Victims Age 3",
           SUM(_5) AS "Victims Age 4",
           SUM(_6) AS "Victims Age 5",
           SUM(_7) AS "Victims Age 6",
           SUM(_8) AS "Victims Age 7",
           SUM(_9) AS "Victims Age 8",
           SUM(_10) AS "Victims Age 9",
           SUM(_11) AS "Victims Age 10",
           SUM(_12) AS "Victims Age 11",
           SUM(_13) AS "Victims Age 12",
           SUM(_14) AS "Victims Age 13",
           SUM(_15) AS "Victims Age 14",
           SUM(_16) AS "Victims Age 15",
           SUM(_17) AS "Victims Age 16 and above"
    FROM healthcare_data 
    GROUP BY state
""", conn)
print("\nQuery - Total number of victims by age group for each state:")
print(query_age_groups)

# Query 1: Count the number of child victims in California aged 5
query1 = pd.read_sql_query("SELECT SUM(_6) AS Victims_Aged_5 FROM healthcare_data WHERE state = 'California'", conn)
print("\nQuery 1 - Count of child victims aged 5 in California:")
print(query1)

# Query 2: Count the number of states with child victims exceeding 500 at age 5
query2 = pd.read_sql_query("SELECT COUNT(DISTINCT state) AS States_Exceeding_500_Aged_5 FROM healthcare_data WHERE _6 > 500", conn)
print("\nQuery 2 - Count of states with child victims exceeding 500 aged 5:")
print(query2)

# Query 3: Calculate the total amount of child victims from each state
query3 = pd.read_sql_query("""
    SELECT state, 
           SUM(_1) + SUM(_2) + SUM(_3) + SUM(_4) + SUM(_5) + 
           SUM(_6) + SUM(_7) + SUM(_8) + SUM(_9) + SUM(_10) + 
           SUM(_11) + SUM(_12) + SUM(_13) + SUM(_14) + 
           SUM(_15) + SUM(_16) + SUM(_17) AS Total_Child_Victims
    FROM healthcare_data
    GROUP BY state
""", conn)
print("\nQuery 3 - Total amount of child victims from each state:")
print(query3)

# Query 4: List the 5 states with the most child victims
query4 = pd.read_sql_query("""
    SELECT state, 
           SUM(_1) + SUM(_2) + SUM(_3) + SUM(_4) + SUM(_5) + 
           SUM(_6) + SUM(_7) + SUM(_8) + SUM(_9) + SUM(_10) + 
           SUM(_11) + SUM(_12) + SUM(_13) + SUM(_14) + 
           SUM(_15) + SUM(_16) + SUM(_17) AS Total_Child_Victims
    FROM healthcare_data
    GROUP BY state
    ORDER BY Total_Child_Victims DESC
    LIMIT 5
""", conn)
print("\nQuery 4 - The 5 states with the most child victims:")
print(query4)

git commit -m "Initial commit with Python script and .gitignore"
git push 