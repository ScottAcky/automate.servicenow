import sqlite3
import pyautogui

# Function to retrieve user details using PyAutoGUI
def retrieve_user_details():
    # Use PyAutoGUI to navigate and retrieve user details
    # Perform actions to get userID, username, contact number, email, location
    # ...

    return userID, username, contact_number, email, location

# Function to retrieve details from ServiceNow database or prompt for input
def get_details_from_database(template):
    conn = sqlite3.connect('servicenow.db')
    cursor = conn.cursor()

    # Check if the template exists in the database
    cursor.execute('''SELECT * FROM servicenow WHERE template = ?''', (template,))
    data = cursor.fetchone()

    if data:
        # Extract details from the retrieved data
        # ...

        # Adjust and update the retrieved long description with dynamic values
        # ...

        # Return updated details
        return updated_short_description, updated_long_description, kb, issue, action
    else:
        # Ask for user input via command prompt
        # Prompt and input data for short_description, long_description, kb, issue, action
        # ...

        # Insert the new data into the database for next time
        # ...

        return new_short_description, new_long_description, new_kb, new_issue, new_action

# Function to update long descriptions with dynamic values
def update_long_description_with_user_details(long_description, userID, username):
    # Update the long description dynamically
    # Replace placeholders with retrieved user details
    updated_long_description = long_description.replace('userID:', f'userID: {userID}') \
                                             .replace('username:', f'username: {username}')
    return updated_long_description

# Function to type out updated_long_description in the description field using PyAutoGUI
def type_out_description(updated_long_description):
    # Click in the description field
    pyautogui.click('description_field.png')  # Replace with the location of your description field

    # Select all in the description field
    pyautogui.hotkey('ctrl', 'a')  # Or any other method to select all in your application

    # Delete the selected text
    pyautogui.press('delete')

    # Type out updated_long_description
    pyautogui.typewrite(updated_long_description)


# Main script
if __name__ == "__main__":
    # Step 1: Retrieve user details using PyAutoGUI
    userID, username, contact_number, email, location = retrieve_user_details()

    # Step 2: Retrieve or prompt for details from ServiceNow database
    template_text = pyautogui.locateCenterOnScreen('template.png')  # Example: Use PyAutoGUI to locate the template
    if template_text:
        # Get details from the database or prompt for input
        short_description, long_description, kb, issue, action = get_details_from_database(template_text)

        # Step 3: Update long descriptions with dynamic values
        updated_long_description = update_long_description_with_user_details(long_description, userID, username)

        # Step 4: Type out updated_long_description into the description field
        type_out_description(updated_long_description)

        # Step 5: Click and paste issue and action
        pyautogui.click('issue_action_location.png')  # Example: Click on the area to paste issue and action
        if issue == action:
            pyautogui.typewrite(issue)
        else:
            pyautogui.typewrite(f"{issue} > {action}")

