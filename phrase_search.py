from tkinter import ttk
import tkinter as tk
from elasticsearch_connection import client

def selections(frm):
    fields = ["Execution", "LastName", "FirstName", "TDCJNumber", "Age", "Race","CountyOfConviction", "AgeWhenReceived", "EducationLevel", "NativeCounty",
            "PreviousCrime", "Codefendants", "NumberVictim ", "WhiteVictim","HispanicVictim", "BlackVictim", "VictimOther Races", "FemaleVictim", "MaleVictim", "LastStatement"]
    ttk.Label(frm, text="Αρχικά θα επιλέξεις σε ποια πεδια θες να αναζητησεις.").grid(column=0, row=1)
    ttk.Label(frm, text="Επιλέξτε το/τα πεδίο/πεδία αναζήτησης:").grid(column=0, row=2)
    choosen = {
        "Execution": {"choosen": tk.BooleanVar()},
        "LastName": {"choosen": tk.BooleanVar()},
        "FirstName": {"choosen": tk.BooleanVar()},
        "TDCJNumber": {"choosen": tk.BooleanVar()},
        "Age": {"choosen": tk.BooleanVar()},
        "Race": {"choosen": tk.BooleanVar()},
        "CountyOfConviction": {"choosen": tk.BooleanVar()},
        "AgeWhenReceived": {"choosen": tk.BooleanVar()},
        "EducationLevel": {"choosen": tk.BooleanVar()},
        "NativeCounty": {"choosen": tk.BooleanVar()},
        "PreviousCrime": {"choosen": tk.BooleanVar()},
        "Codefendants": {"choosen": tk.BooleanVar()},
        "NumberVictim ": {"choosen": tk.BooleanVar()},
        "WhiteVictim": {"choosen": tk.BooleanVar()},
        "HispanicVictim": {"choosen": tk.BooleanVar()},
        "BlackVictim": {"choosen": tk.BooleanVar()},
        "VictimOther Races": {"choosen": tk.BooleanVar()},
        "FemaleVictim": {"choosen": tk.BooleanVar()},
        "MaleVictim": {"choosen": tk.BooleanVar()},
        "LastStatement": {"choosen": tk.BooleanVar()}
    } 
    #PROSWRINA AI HELP SE AFTO TO SHMEIO GIA NA PROXWRAME
    for i in range(0, 19):
        # Create a BooleanVar for the checkbox
        choosen[fields[i]]["choosen"] = tk.BooleanVar()
        ttk.Checkbutton(
            frm, text=fields[i], variable=choosen[fields[i]]["choosen"]
        ).grid(row=i, column=1)
    #PROSWRINA AI HELP SE AFTO TO SHMEIO GIA NA PROXWRAME
    """
    for i in range(0,19):
        choosen[fields[i]]["choosen"]=tk.BooleanVar()
        ttk.Checkbutton(frm, text=fields[i], variable=choosen[fields[i]]["choosen"]).grid(row=i, column=1)
        choosen[fields[i]]["type"] = tk.StringVar(value="not_choosen")
        ttk.Radiobutton(frm, text="Must", variable=choosen[fields[i]].update({"type":"must"}), value="must").grid(row=i, column=2)
        ttk.Radiobutton(frm, text="Should", variable=choosen[fields[i]].update({"type":"should"}), value="should").grid(row=i, column=3)
        ttk.Radiobutton(frm, text="Must Not", variable=choosen[fields[i]].update({"type":"must-not"}), value="must-not").grid(row=i, column=4)
    """
    ttk.Button(frm, text="Υποβολή", command=lambda: construct_query(choosen, fields, frm)).grid(column=0, row=19)

def construct_query(choosen, fields, frm):
    entries = []
    for element in frm.winfo_children():
        element.destroy()
    i=20
    j=0
    for i, field in enumerate(fields):
        if choosen[field]["choosen"].get():
            entries.append(tk.StringVar())
            ttk.Label(frm, text="Πεδίο: "+ field).grid(column=0, row=i)
            #ttk.Label(frm, text="Τύπος: "+ choosen[field]["type"].get()).grid(column=0, row=i+1)
            ttk.Entry(frm, width=50, textvar=entries[j], textvariable=entries[j]).grid(column=1, row=i)
            j+=1
    ttk.Button(frm, text="Υποβολή", command=lambda: construct_query2(choosen, fields, entries)).grid(column=0, row=23)

    
def construct_query2(choosen, fields, entries):
    query = {
            "match_phrase": {
                "Execution": [],
                "LastName": [],
                "FirstName": [],
                "TDCJNumber": [],
                "Age": [],
                "Race": [],
                "CountyOfConviction": [],
                "AgeWhenReceived": [],
                "EducationLevel": [],
                "NativeCounty": [],
                "PreviousCrime": [],
                "Codefendants": [],
                "NumberVictim ":[],
                "WhiteVictim": [],
                "HispanicVictim": [],
                "BlackVictim": [],
                "VictimOther Races": [],
                "FemaleVictim": [],
                "MaleVictim": [],
                "LastStatement": []
            }
        }
    j=0
    for i,field in enumerate(fields):
        if choosen[field]["choosen"].get():
            text = {"{field}": {entries[j].get()}}
            query["match_phrase"][field].append(text)
            j+=1
    print(query)
    print("EPITUXWS TO SEARCH") 

    
def execute_search(query):
    resp = client.search(query)
    print("Phrase search results:")
    print(resp)