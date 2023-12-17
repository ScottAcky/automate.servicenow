import sqlite3
import pyperclip

# Function to retrieve and copy the "Long Description (Updated)" from the servicenow database to the clipboard
def copy_long_description_update_to_clipboard():
    conn = sqlite3.connect('servicenow.db')
    cursor = conn.cursor()

    # Selecting only the "Long Description (Updated)" column from the servicenow table
    cursor.execute('''SELECT long_description_update FROM servicenow''')
    long_description_update = cursor.fetchone()

    # Check if data exists and copy to clipboard
    if long_description_update:
        description_text = long_description_update[0]
        pyperclip.copy(description_text)
        print("Long Description (Updated) copied to clipboard:")
        print(description_text)
    else:
        print("No Long Description (Updated) found.")

    # Close connection
    conn.close()

# Call the function to retrieve and copy the "Long Description (Updated)" to the clipboard
copy_long_description_update_to_clipboard()
