# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk 
from tkinter import ttk,filedialog
from elasticsearch_connection import client
import json

def addremove_menu():
    main_window = tk.Tk()
    main_window.title("Add or remove data from file")
    delete_Entry=tk.StringVar()
    frm = ttk.Frame(main_window, padding=10)
    frm.grid()
    ttk.Label(frm, text="Επέλεξε αρχείο:").grid(column=0, row=0)    
    ttk.Button(frm,text="Browse..",command=add_from_file).grid(column=1,row=0)
    ttk.Label(frm, text="Διέγραψε κάποιον:").grid(column=0, row=1)
    tk.Entry(frm,textvariable=delete_Entry, width=50).grid(column=1,row=1)
    ttk.Button(frm,text="Delete",command=remove_from_index).grid(column=2,row=1)
    ttk.Button(frm,text="Delete Index",command=remove_index).grid(column=0,row=2)
    main_window.mainloop()

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("JSON Files", "*.json"), ("Text Files", "*.txt")],
        title="Select a File"
    )
    print(file_path)
    return file_path

def add_from_file():
    try:
        input_file = open(select_file(), "r")
    except FileNotFoundError:
        print("Could not find the file")
        return
    except PermissionError:
        print("You have no permission to read this file")
        return
    try:
        next(input_file)
        for line in input_file:
            doc=line.strip().split(',',19)
            if not doc[3].isdigit():
                right_name=doc[1]+doc[2]
                doc1=line.strip().split(',',20)
                for i in range(1, 20):
                    if i==1:
                        doc1[i]=right_name
                    else:
                        doc1[i]=doc1[i+1]
                print(doc1)
                doc=doc1

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
    except Exception as e:
        print("Minor error occured")
    
        print(f"Indexed from file!")
        
def remove_from_index():
    doc_to_remove=delete_Entry.get()
    try:
        
        client.delete(index="last_statement", id=doc_to_remove)
        print("Removed doc ",doc_to_remove)
    except Exception as e:
        print("Error could not find the doc that you were looking for")

def remove_index():
    try:
        
        client.indices.delete(index="last_statement")
        print("Deleting index..")
    except Exception as e:
        print("Error could not find the index you were looking for,you can add files to make one")
