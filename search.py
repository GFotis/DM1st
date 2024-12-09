# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
from indexing_and_preprocessing import indexing_and_preprocessing
from elasticsearch_connection import client

def search_menu():
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    global frm
    frm = ttk.Frame(main_window, padding=10)
    indexing_and_preprocessing()
    frm.grid()
    ttk.Label(frm, text="Επέλεξε με ποιο μοντέλο θέλεις να γίνει η αναζήτηση:").grid(column=0, row=0)
    ttk.Button(frm, text="Boolean Model ", command=searching_boolean()).grid(column=1, row=0)
    ttk.Button(frm, text="VSM Model ", command=searching_vsm).grid(column=2, row=0)
    ttk.Button(frm, text="Έξοδος", command=main_window.destroy).grid(column=3, row=0)
    main_window.mainloop()

def searching_vsm():
    resp = client.search(index="l ast_statement", query={"match_all": {}})
    for hit in resp['hits']['hits']:
        print(f"Αναζήτηση: {hit['_source']}")

def searching_boolean():
    for element in frm.winfo_children():
        element.destroy()
    selections()

def selections():
    fields = ["Execution", "LastName", "FirstName", "TDCJNumber", "Age", "Race","CountyOfConviction", "AgeWhenReceived", "EducationLevel", "NativeCounty",
            "PreviousCrime", "Codefendants", "NumberVictim ", "WhiteVictim","HispanicVictim", "BlackVictim", "VictimOther Races", "FemaleVictim", "MaleVictim", "LastStatement"]
    ttk.Label(frm, text="Αρχικά θα επιλέξεις σε ποια πεδια θες να αναζητησεις.").grid(column=0, row=1)
    ttk.Label(frm, text="Επιλέξτε το/τα πεδίο/πεδία αναζήτησης:").grid(column=0, row=2)
    choosen = {
        "Execution": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "LastName": {"choosen": tk.BooleanVar(), "type":  tk.StringVar()},
        "FirstName": {"choosen": tk.BooleanVar(), "type": tk.StringVar() },
        "TDCJNumber": {"choosen": tk.BooleanVar(), "type":  tk.StringVar()},
        "Age": {"choosen": tk.BooleanVar(), "type": tk.StringVar() },
        "Race": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "CountyOfConviction": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "AgeWhenReceived": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "EducationLevel": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "NativeCounty": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "PreviousCrime": {"choosen": tk.BooleanVar(), "type":  tk.StringVar()},
        "Codefendants": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "NumberVictim ": {"choosen": tk.BooleanVar(), "type":  tk.StringVar()},
        "WhiteVictim": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "HispanicVictim": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "BlackVictim": {"choosen": tk.BooleanVar(), "type":  tk.StringVar()},
        "VictimOther Races": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "FemaleVictim": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "MaleVictim": {"choosen": tk.BooleanVar(), "type": tk.StringVar()},
        "LastStatement": {"choosen": tk.BooleanVar(), "type": tk.StringVar()}
    } 
    #PROSWRINA AI HELP SE AFTO TO SHMEIO GIA NA PROXWRAME
    for i in range(0, 19):
        # Create a BooleanVar for the checkbox
        choosen[fields[i]]["choosen"] = tk.BooleanVar()
        ttk.Checkbutton(
            frm, text=fields[i], variable=choosen[fields[i]]["choosen"]
        ).grid(row=i, column=1)

        # Create a StringVar for the radiobutton group
        choosen[fields[i]]["type"] = tk.StringVar(value="not-choosen")  # Default to "must"

        # Radiobuttons for "must", "should", and "must-not"
        ttk.Radiobutton(
            frm, text="Must", variable=choosen[fields[i]]["type"], value="must"
        ).grid(row=i, column=2)
        ttk.Radiobutton(
            frm, text="Should", variable=choosen[fields[i]]["type"], value="should"
        ).grid(row=i, column=3)
        ttk.Radiobutton(
            frm, text="Must Not", variable=choosen[fields[i]]["type"], value="must-not"
        ).grid(row=i, column=4)
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
    ttk.Button(frm, text="Υποβολή", command=lambda: construct_query(choosen, fields)).grid(column=0, row=19)

def construct_query(choosen, fields):
    entries = []
    for element in frm.winfo_children():
        element.destroy()
    i=20
    j=0
    for i, field in enumerate(fields):
        if choosen[field]["choosen"].get():
            entries.append(tk.StringVar())
            ttk.Label(frm, text="Πεδίο: "+ field).grid(column=0, row=i)
            ttk.Label(frm, text="Τύπος: "+ choosen[field]["type"].get()).grid(column=0, row=i+1)
            ttk.Entry(frm, width=50, textvar=entries[j], textvariable=entries[j]).grid(column=1, row=i)
            j+=1
    ttk.Button(frm, text="Υποβολή", command=lambda: construct_query2(choosen, fields, entries)).grid(column=0, row=23)

def construct_query2(choosen, fields, entries):
    """
    j=0
    match_text = None
    type_text = None
    query = {
        "query": {
            "bool": { 
                
             }
            }
        }
    """
    must_text=None
    should_text=None
    must_not_text=None
    query ={
        "query": {
            "bool": {
                "must": [],
                "should": [],
                "must_not": []
            }
        }
    }
    j=0
    for i,field in enumerate(fields):
        if choosen[field]["choosen"].get():
            if choosen[field]["type"].get() == "must":
                must_text = {"match": {field: entries[j].get()}}
                query["query"]["bool"]["must"].append(must_text)
            elif choosen[field]["type"].get() == "must_not":
                must_not_text = {"match": {field: entries[j].get()}}
                query["query"]["bool"]["should"].append(must_not_text)
            else:
                should_text = {"match": {field: entries[j].get()}}
                query["query"]["bool"]["should"].append(should_text)
            j+=1
    print(query)
    print("EPITUXWS TO SEARCH") 

def extract_string(entry):
    return 