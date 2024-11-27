import spacy
from preproccess import preproccess_input_data

import os
index={}
#print(os.path.exists("C:\Users\dimit\Desktop\python_functions\Texas_Last_Statement.csv"))
with open('C:/Users/dimit/Desktop/python_functions/Texas_Last_Statement.csv', 'r') as input_file:
        # Skip the first line (header)
        next(input_file)
        # Process each line
        for row_number, line in enumerate(input_file, start=1):
                index = preproccess_input_data(line, row_number, index)

for word, rows in index.items():
        print(f"{word}: {rows}")









