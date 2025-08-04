import re  # Import the regular expression module

# Define a function to extract emails from a given file
def extract_emails(filename):
    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
        
        # Use regex to find all email addresses in the file content
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        
        if emails:
            print("Found these email addresses:")
            for email in set(emails):  # Use set to remove duplicates
                print(f"- {email}")
        else:
            print("No email addresses found in the file.")
    
    except FileNotFoundError:
        # If the file doesn't exist, print an error message
        print(f"File not found: {filename}")

# Only run this part if the script is being executed directly
if __name__ == "__main__":
    # Ask the user to enter the filename (e.g., sample.txt)
    filename = input("Enter the name of the text file (including extension): ")
    extract_emails(filename)  # Call the function with the user's input

# Pause the program so the window doesn't close immediately
input("\nPress Enter to exit...")

