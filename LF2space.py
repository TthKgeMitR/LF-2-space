import pyperclip
import re

input_string = pyperclip.paste()
output_string  = re.sub(r"\r\n|\r|\n", " ", input_string).replace("  ", " ")

pyperclip.copy(output_string)
print(output_string)
