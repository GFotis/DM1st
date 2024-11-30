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
        line_rmst=remove_stopwords(doc[19])
        client.indices.analyze(tokenizer="standard", filter=["stemmer"], text=line_rmst.lower())
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
            "LastStatement": line_rmst
        }
        
        json_file=json.dumps(temp)
        client.index(index="last_statement", document=json_file, ignore=400)
        print(f"Indexed document ID {doc}")
    input_file.close()

def remove_stopwords(line):
    file=open("stopwords.txt", "r")
    words = line.split(r"[, \n]")
    stopwords = file.read().split(r"[, \n]")
    for word in words:
        if word in stopwords:
            words.remove(word)
    return " ".join(words)