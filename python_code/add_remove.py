# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk, Label,  Button, filedialog, messagebox # Dictionary for the GUI application
from tkinter.ttk import Entry
from elasticsearch_connection import client

# GUI
import json
#client.indices.delete(index="last_statement")
def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("JSON Files", "*.json"), ("Text Files", "*.txt")],
        title="Select a File"
    )
    return file_path
def add_from_file():
    input_file = open(select_file(), "r")
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
def remove_from_index():
    doc_to_remove=delete_Entry.get()
    print(doc_to_remove)
    client.delete(index="last_statement", id=doc_to_remove)

def remove_index():
    print("Deleting index..")
    client.indices.delete(index="last_statement")

root = tk.Tk()
root.title("Add or remove data from file")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Επέλεξε αρχείο:").grid(column=0, row=0)    
ttk.Button(frm,text="Browse..",command=select_file).grid(column=1,row=0)
ttk.Label(frm, text="Διέγραψε κάποιον:").grid(column=0, row=1)
delete_Entry=Entry(frm, width=50).grid(column=1,row=1)
ttk.Button(frm,text="Delete",command=remove_from_index).grid(column=2,row=1)


root.mainloop()



    #client.indices.delete(index="last_statement")
    #client.update(
   #     index="last_statement",
    #    id="2",
   #     doc={
    #        "LastName": "Bond"
            
   #     },
   # )
   # client.delete(index="last_statement", id=doc_id)