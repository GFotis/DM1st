# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
from elasticsearch_connection import client
# GUI
import json
#client.indices.delete(index="last_statement")
def add_from_file(file_path):
    input_file = open(file_path, "r")
    next(input_file)
    for line in input_file:
        doc=line.strip().split(',',19)
        
        
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
        client.index(index="last_statement",id=doc[0], document=json_file)
        print(f"Indexed document ID {doc}")
def remove_from_index(doc_to_remove):
    print(doc_to_remove)
    client.delete(index="last_statement", id=doc_to_remove)

    #client.indices.delete(index="last_statement")
    #client.update(
   #     index="last_statement",
    #    id="2",
   #     doc={
    #        "LastName": "Bond"
            
   #     },
   # )
   # client.delete(index="last_statement", id=doc_id)