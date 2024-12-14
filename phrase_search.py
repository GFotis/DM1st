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
    ttk.Button(frm, text="Υποβολή", command=lambda: construct_query2(choosen, fields, entries, frm)).grid(column=0, row=23)

    
def construct_query2(choosen, fields, entries, frm):
    query ={
        "query": {
            "bool": {
                "must": []
            }
        }
    }
    j=0
    for i,field in enumerate(fields):
        if choosen[field]["choosen"].get():
            text = {"match_phrase": {field:  entries[j].get()}}
            query["query"]["bool"]["must"].append(text)
            #must_text = {"match": {field: entries[j].get()}}
              #  query["query"]["bool"]["must"].append(must_text)
            j+=1
    print(query)
    print("EPITUXWS TO SEARCH") 
    execute_search(query, frm)

def execute_search(query, frm):
    resp = client.search(index="last_statement", body=query)
    ttk.Label(frm, text=f"Βρέθηκαν {resp['hits']['total']['value']} αποτελέσματα").grid(column=0, row=5)  
    #print_results(resp)

def print_results(resp):
    main_window = tk.Tk()
    main_window.geometry("1366x768") 
    main_window.title("Search Results")
    frm = ttk.Frame(main_window, padding=10)
    frm.grid()
    ttk.Label(frm, text="Αποτελέσματα Αναζήτησης:").grid(column=0, row=0)
    #i = 1  
   # for hit in resp["hits"]["hits"]:
     #   ttk.Label(frm, text=hit["_source"]).grid(column=0, row=i)
     #   i += 1
    #main_window.mainloop()