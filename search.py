# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
from indexing_and_preprocessing import indexing_and_preprocessing
from elasticsearch_connection import client
import boolean_search as bs
import vsm_search as vsm

def destroy_all_widgets():
    for widget in frm.winfo_children():
        widget.destroy()

def return_to_main_menu():
    destroy_all_widgets()

def cancel_search():
    destroy_all_widgets()
    search_menu()

def search_menu():
    global frm
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    frm = ttk.Frame(main_window, padding=10)
    indexing_and_preprocessing()
    frm.grid()
    ttk.Label(frm, text="Επέλεξε με ποιο μοντέλο θέλεις να γίνει η αναζήτηση:").grid(column=0, row=0)
    ttk.Button(frm, text="Boolean Model ", command=searching_boolean).grid(column=1, row=3)
    ttk.Button(frm, text="VSM Model ", command=searching_vsm).grid(column=2, row=3)
    ttk.Button(frm, text="Έξοδος", command=return_to_main_menu).grid(column=3, row=3)
    main_window.mainloop()

def searching_vsm():
    destroy_all_widgets()
    vsm.selections(frm)

def searching_boolean():
    destroy_all_widgets()
    bs.selections(frm)