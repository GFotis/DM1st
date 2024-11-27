# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr
import spacy
def preproccess_input_data(line, row_number, index):
    last_column = line.split(',')[-1].strip()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(last_column)
    lemmas = [token.lemma_ for token in doc]
    print("Lemmatized text:", " ".join(lemmas))
    
    
    for word in lemmas:
        if word not in index:
            index[word] = []
        index[word].append(row_number)
    return index