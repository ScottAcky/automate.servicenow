import sqlite3

# Connect to the database
conn = sqlite3.connect('servicenow.db')  # Replace 'your_database_name.db' with your database file name
cursor = conn.cursor()

# Execute a query to select all data from a specific table (e.g., servicenow)
cursor.execute('''SELECT * FROM servicenow''')  # Replace 'servicenow' with your table name
data = cursor.fetchall()

# Display retrieved data
for row in data:
    print(row)

# Close connection
conn.close()

