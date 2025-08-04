import re

def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        if emails:
            print("Found these email addresses:")
            for email in set(emails):
                print(f"- {email}")
        else:
            print("No email addresses found in the file.")
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    filename = input("Enter the name of the text file (including extension): ")
    extract_emails(filename)
