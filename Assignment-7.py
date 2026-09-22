import re

text = """
Please contact us at john@example.com or support@gmail.com.
You can also email admin@college.edu.in for further information.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)