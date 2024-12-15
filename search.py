# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
from indexing_and_preprocessing import indexing_and_preprocessing
from elasticsearch_connection import client
import boolean_search as bs
import vsm_search as vsm
import phrase_search as ps

def search_menu():
    main_window = tk.Toplevel()
    main_window.title("Which Model???")
    main_window.geometry("1366x768")
    frm = ttk.Frame(main_window, padding=10)
    indexing_and_preprocessing()
    frm.grid()
    ttk.Label(frm, text="Επέλεξε με ποιο μοντέλο θέλεις να γίνει η αναζήτηση:").grid(column=0, row=0)
    ttk.Button(frm, text="Boolean Model ", command=searching_boolean).grid(column=1, row=3)
    ttk.Button(frm, text="VSM Model ", command=searching_vsm).grid(column=2, row=3)
    ttk.Button(frm, text="Phrase Model ", command=searching_phrase).grid(column=3, row=3)
    ttk.Button(frm, text="Επιστροφή", command=main_window.destroy).grid(column=4, row=3)
    main_window.mainloop()

def searching_vsm():
    vsm.selections()

def searching_boolean():
    bs.selections()

def searching_phrase():
    ps.selections()