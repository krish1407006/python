# Regular expression in Python

import re

# Example 1: Check if a string starts with "Hello"
text = "Hello, how are you?"
pattern = r'^Hello'
if re.match(pattern, text):
    print("The string starts with 'Hello'")


# Example 2: Find all email addresses in a string
text2 = "Contact us at info@example.com or support@domain.org."
pattern2 = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern2, text2)
print("Email addresses found:", emails)

# Example 3: Extract all numbers from a string
text3 = "Order 1234 costs $56 and order 5678 costs $78."
pattern3 = r'\d+'
numbers = re.findall(pattern3, text3)
print("Numbers found:", numbers)

# Example 4: Replace all whitespace with a dash
text4 = "Python regular expressions are powerful!"
pattern4 = r'\s+'
replaced = re.sub(pattern4, '-', text4)
print("Whitespace replaced:", replaced)

# Example 5: Validate a phone number (simple US format)
text5 = "Call me at 123-456-7890."
pattern5 = r'\b\d{3}-\d{3}-\d{4}\b'
match = re.search(pattern5, text5)
if match:
    print("Phone number found:", match.group())

# Example 6: Check if a string is a valid date (YYYY-MM-DD)
text6 = "2026-05-20"
pattern6 = r'^\d{4}-\d{2}-\d{2}$'
if re.match(pattern6, text6):
    print("Valid date format!")

# Example 7: Find all words starting with a capital letter
text7 = "Python is Fun and Powerful."
pattern7 = r'\b[A-Z][a-z]*\b'
words = re.findall(pattern7, text7)
print("Capitalized words:", words)
