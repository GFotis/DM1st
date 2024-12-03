# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
from indexing_and_preprocessing import indexing_and_preprocessing
from elasticsearch_connection import client
import elasticsearch

def search_menu():
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    global frm
    frm = ttk.Frame(main_window, padding=10)
    indexing_and_preprocessing()
    frm.grid()
    ttk.Label(frm, text="Επέλεξε με ποιο μοντέλο θέλεις να γίνει η αναζήτηση:").grid(column=0, row=0)
    ttk.Button(frm, text="Boolean Model ", command=searching_boolean).grid(column=1, row=0)
    ttk.Button(frm, text="VSM Model ", command=searching_vsm).grid(column=2, row=0)
    ttk.Button(frm, text="Έξοδος", command=main_window.destroy).grid(column=3, row=0)
    main_window.mainloop()

def searching_vsm():
    resp = client.search(index="l ast_statement", query={"match_all": {}})
    for hit in resp['hits']['hits']:
        print(f"Αναζήτηση: {hit['_source']}")

def searching_boolean():
    #frm.destroy()
    final_query = None
    for element in frm.winfo_children():
        element.destroy()
    search_entry = selections(final_query)
    #search_entry = ttk.Entry(frm, width=50)
    client.search(index="last_statement", body=search_entry, ignore=400)
    print("EPITUXWS TO SEARCH")
    pass

def flag_true(flag):
        flag=True

def selections(final_query):
    fields = ["Execution", "LastName", "FirstName", "TDCJNumber", "Age", "Race","CountyOfConviction", "AgeWhenReceived", "EducationLevel", "NativeCounty",
            "PreviousCrime", "Codefendants", "NumberVictim ", "WhiteVictim","HispanicVictim", "BlackVictim", "VictimOther Races", "FemaleVictim", "MaleVictim", "LastStatement"]
    ttk.Label(frm, text="Αρχικά θα επιλέξεις σε ποια πεδια θες να αναζητησεις.").grid(column=0, row=1)
    ttk.Label(frm, text="Επιλέξτε το/τα πεδίο/πεδία αναζήτησης:").grid(column=0, row=2)
    choosen = {
        "Execution": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "LastName": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "FirstName": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "TDCJNumber": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "Age": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "Race": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "CountyOfConviction": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "AgeWhenReceived": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "EducationLevel": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "NativeCounty": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "PreviousCrime": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "Codefendants": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "NumberVictim ": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "WhiteVictim": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "HispanicVictim": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "BlackVictim": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "VictimOther Races": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "FemaleVictim": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "MaleVictim": {"choosen": tk.IntVar(), "type": "not_choosen"},
        "LastStatement": {"choosen": tk.IntVar(), "type": "not_choosen"}
    }
    for i in range(0,19):
        choosen[fields[i]]["choosen"]=tk.IntVar()
        ttk.Checkbutton(frm, text=fields[i]).grid(row=i, column=1)
        choosen[fields[i]]["type"] = tk.StringVar()
        ttk.Radiobutton(frm, text="Must", variable=choosen[fields[i]]["type"], value="must").grid(row=i, column=2)
        ttk.Radiobutton(frm, text="Should", variable=choosen[fields[i]]["type"], value="should").grid(row=i, column=3)
        ttk.Radiobutton(frm, text="Must Not", variable=choosen[fields[i]]["type"], value="must_not").grid(row=i, column=4)
        choosen[fields[i]]["type"].set("not_choosen")
    ttk.Button(frm, text="Υποβολή", command=lambda: construct_query(choosen, fields, final_query)).grid(column=0, row=19)
     
def construct_query(choosen, fields, final_query):
    query = None
    for i in range(0,19):
        if choosen[fields[i]]["choosen"].get() == 1:
            search_entry = ttk.Entry(frm, width=50)
            search_entry.grid(column=1, row=20)
            query="{query:{ bool: "+choosen[fields[i]]["type"]+"{: {match:"+ {fields[i]: search_entry.get()}+"}}}}"
            """
            query = {
                    "query": {
                        "bool": {choosen[fields[i]]["type"]: {
                                    "match": {fields[i]: search_entry.get()
                                    }
                                }
                        }
                    }
            }
            """
    final_query = query