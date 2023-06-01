import re

def convert_text(file_path):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Convert the text to lowercase
    lowercase_text = text.lower()

    # Remove symbols using regular expressions
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', lowercase_text)

    return cleaned_text

# Example usage
file_path = 'path/to/your/file.txt'  # Replace with the actual path to your text file
converted_text = convert_text(file_path)
print(converted_text)
