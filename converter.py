import re

def convert_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9]', '', text)
    return text

# Read input text from file
file_path = "corrected_sentence.txt"  # Update with the path to your input file

with open(file_path, "r") as file:
    input_text = file.read()

# Convert the text
converted_text = convert_text(input_text)

# Write converted text to file
output_file_path = "output.txt"  # Update with the path to your output file

with open(output_file_path, "w") as file:
    file.write(converted_text)

print("Conversion complete. Converted text saved to:", output_file_path)
