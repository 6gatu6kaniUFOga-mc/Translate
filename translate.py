# Import the googletrans library
from googletrans import Translator

# Create a translator object
translator = Translator()

# Define a function to translate a text from Russian to Japanese
def translate(text):
    # Use the translator object to translate the text and return the result
    return translator.translate(text, src="ru", dest="ja").text

# Open the language configuration file in read mode
with open("language.yml", "r") as file:
    # Read the file content and store it in a variable
    content = file.read()

# Split the content by lines
lines = content.split("\n")

# Create an empty list to store the translated lines
translated_lines = []

# Iterate over each line
for line in lines:
    # If the line starts with "#" or is empty, do not translate it
    if line.startswith("#") or line == "":
        translated_lines.append(line)
    # Otherwise, translate the line and append it to the list
    else:
        # Split the line by ":" and translate the second part
        key, value = line.split(":")
        translated_value = translate(value)
        # Join the key and the translated value with ":" and append it to the list
        translated_line = key + ":" + translated_value
        translated_lines.append(translated_line)

# Join the translated lines with "\n" and store it in a variable
translated_content = "\n".join(translated_lines)

# Print the translated content
print(translated_content)
