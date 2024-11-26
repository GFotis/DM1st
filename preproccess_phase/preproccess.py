# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

def preproccess_input_data(line, row_number, index):
    last_column = line.split(',')[-1].strip()
    words = last_column.split()
    for word in words:
        if word not in index:
            index[word] = []
        index[word].append(row_number)
    return index