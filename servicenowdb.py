import sqlite3

# Function to create the servicenow database and table structure
def create_servicenow_database():
    conn = sqlite3.connect('servicenow.db')
    cursor = conn.cursor()

    # Create a table for servicenow
    cursor.execute('''CREATE TABLE IF NOT EXISTS servicenow (
                        id INTEGER PRIMARY KEY,
                        template TEXT,
                        short_description TEXT,
                        long_description TEXT,
                        kb_number TEXT,
                        description TEXT,
                        action_taken TEXT,
                        long_description_update TEXT)''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to insert the provided data into the servicenow database
def insert_servicenow_content(template, short_desc, long_desc, kb_num, description, action_taken, long_desc_update):
    conn = sqlite3.connect('servicenow.db')
    cursor = conn.cursor()

    # Insert data into the servicenow table
    cursor.execute('''INSERT INTO servicenow (template, short_description, long_description, kb_number, description, action_taken, long_description_update)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (template, short_desc, long_desc, kb_num, description, action_taken, long_desc_update))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Create the servicenow database and table structure
create_servicenow_database()

# Inserting the provided content into the servicenow database
insert_servicenow_content(
    "Active Directory - Password Reset",
    "Active Directory - Password Reset",
    "** ALL FIELDS BELOW ARE REQUIRED WHEN COMPLETING TICKETS **\nUser ID:\nUser Name:\nContact Number:\nEmail:\nLocation:\n\nKBA: KB0012023\nKBA checked : Yes/No\n\nPassword Reset Complete: Yes / No\nAccess Restored: Yes / No\n\nNote: Any user who is registered for MFA should be advised and educated on how to utilise the SSPR process.\n\nAction Taken: ",
    "KB0012023",
    "User called unable to login as they had forgotten their password > guided user through steps to change password > confirmed password changed > access restored > issue resolved",
    "User called unable to login as they had forgotten their password > guided user through steps to change password > confirmed password changed > access restored > issue resolved",
    "User ID:\nUser Name:\nContact Number:\nEmail:\nLocation:\n\nKBA: KB0012023\nKBA checked : Yes\n\nPassword Reset Complete: Yes\nAccess Restored: Yes\n\nNote: Any user who is registered for MFA should be advised and educated on how to utilise the SSPR process.\n\nAction Taken: User called unable to login as they had forgotten their password > guided user through steps to change password > confirmed password changed > access restored > issue resolved"
)

