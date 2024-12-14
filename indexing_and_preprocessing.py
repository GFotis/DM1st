# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

from elasticsearch_connection import client
import json
import pandas 

#PROSWRINA ME PANDAS GIA NA PROXWRISEI TO PROJECT

def indexing_and_preprocessing():
    #input_file = open("input_data\\Texas Last Statement.csv", "r")
    if client.indices.exists(index="last_statement"):
        print("Έχει ήδη γίνει εισαγωγή των δεδομένων στΟ Elasticsearch!")
        return
    input_file=pandas.read_csv("input_data\\Texas Last Statement.csv")
    #next(input_file)
    sum=0
    for _,line in input_file.iterrows():
        #doc=line.strip().split(',',19)
        #if len(doc)!=20:
           # continue
        #line_rmst=remove_stopwords(doc[19]) PROSWRINA EKTOS LEITOURGIAS
        #client.indices.analyze(tokenizer="standard", filter=["stemmer"], text=input_file[19].str.lower())
        temp={
            "Execution": line['Execution'],
            "LastName": line['LastName'],
            "FirstName": line['FirstName'],
            "TDCJNumber": line['TDCJNumber'],
            "Age": line['Age'],
            "Race": line['Race'],
            "CountyOfConviction": line['CountyOfConviction'],
            "AgeWhenReceived": line['AgeWhenReceived'],
            "EducationLevel": line['EducationLevel'],
            "NativeCounty": line['NativeCounty '],
            "PreviousCrime": line['PreviousCrime'],
            "Codefendants": line['Codefendants'],
            "NumberVictim": line['NumberVictim'],
            "WhiteVictim": line['WhiteVictim'],
            "HispanicVictim": line['HispanicVictim'],
            "BlackVictim": line['BlackVictim'],
            "VictimOther Races": line['VictimOther Races'],
            "FemaleVictim": line['FemaleVictim'],
            "MaleVictim": line['MaleVictim'],
            "LastStatement": line['LastStatement']
        }
        sum+=1
        json_file=json.dumps(temp)
        client.index(index="last_statement", document=json_file, ignore=400)
        #print(f"Indexed document ID {doc}")
    #input_file.close()
    print(f"Indexed {sum} documents")

def remove_stopwords(line):
    file=open("stopwords.txt", "r")
    words = line.split(r"[, \n]")
    stopwords = file.read().split(r"[, \n]")
    for word in words:
        if word in stopwords:
            words.remove(word)
    return " ".join(words)