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
    ttk.Label(frm, text="Εισάγετε το κείμενο που θέλετε να αναζητήσετε:").grid(column=0, row=1)
    search_entry = ttk.Entry(frm, width=50)
    
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"LastStatement": fields["must"]}}  # Must match 'must' term in LastStatement
                ],
                "should": [
                    {"match": {"FirstName": fields["should"]}},  # Should match 'should' term in FirstName
                    {"match": {"LastName": fields["should"]}}   # Should match 'should' term in LastName
                ],
                "must_not": [
                    {"match": {"LastName": fields["must_not"]}}  # Must not match 'must_not' term in LastName
                ]
            }
        }
    }
    pass