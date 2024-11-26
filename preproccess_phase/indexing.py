# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr
from .preproccess import preproccess_input_data

def create_index():
    # Initialize index dictionary
    index = {}

    # Open the data file
    with open('input_data\\Texas Last Statement.csv', 'r') as input_file:
        # Skip the first line (header)
        next(input_file)
        # Process each line
        for row_number, line in enumerate(input_file, start=1):
            index = preproccess_input_data(line, row_number, index)

    # Print index
    for word, rows in index.items():
        print(f"{word}: {rows}")