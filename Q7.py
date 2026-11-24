"""Question 7: Find and extract valid email addresses using regex."""

import re


def extract_email_addresses(text):
    """Return unique valid-looking email addresses found in text."""
    pattern = r"(?<![\w.+-])[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+(?![\w.-])"
    return re.findall(pattern, text)


if __name__ == "__main__":
    file_name = input("Enter input text-file name: ").strip()
    try:
        with open(file_name, "r", encoding="utf-8") as input_file:
            content = input_file.read()
    except FileNotFoundError:
        print("File not found.")
    else:
        emails = extract_email_addresses(content)
        if emails:
            print("Valid email addresses found:")
            for email in emails:
                print(email)
        else:
            print("No valid email addresses found.")
