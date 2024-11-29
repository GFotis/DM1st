# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr
from elasticsearch_connection import client
import json

def indexing_and_preprocessing():
    input_file = open("input_data\\Texas Last Statement.csv", "r")
    next(input_file)
    for line in input_file:
        doc=line.strip().split(',')
        if len(doc)!=20:
            continue
        temp={
            "Execution": doc[0],
            "LastName": doc[1],
            "FirstName": doc[2],
            "TDCJNumber": doc[3],
            "Age": doc[4],
            "Race": doc[5],
            "CountyOfConviction": doc[6],
            "AgeWhenReceived": doc[7],
            "EducationLevel": doc[8],
            "NativeCounty": doc[9],
            "PreviousCrime": doc[10],
            "Codefendants": doc[11],
            "NumberVictim": doc[12],
            "WhiteVictim": doc[13],
            "HispanicVictim": doc[14],
            "BlackVictim": doc[15],
            "VictimOther Races": doc[16],
            "FemaleVictim": doc[17],
            "MaleVictim": doc[18],
            "LastStatement": doc[19]
        }
        json_file=json.dumps(temp)
        client.index(index="evretirio", document=json_file, ignore=400)
        print(f"Indexed document ID {doc}")
    """
        # Initialize index dictionary
    global index
    index = {}
    client.indices.create(index='Evretirio', ignore=400)
    with open('stopwords.txt', 'r') as stopwords_file:
        stopwords = set()
        for line in stopwords_file:
            stopwords.add(line.strip().lower())

    def preproccess_input_data(line, row_number, index):
        words = line.split(',') 
        for word in words:
            word = word.strip()
            word = word.lower()
            if word in stopwords:
                continue
            if word not in index:
                index[word] = []
            index[word].append(row_number)
    return index

def convert_to_json():
    json_file = open("input.json", "wr")
    input_file = open("input_data\\Texas Last Statement.csv", "rt")
    next(input_file)
    for line in input_file:
        json_file.write(json.dumps(line))
    return json_file
    """