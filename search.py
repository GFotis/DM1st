# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
from indexing_and_preprocessing import indexing_and_preprocessing

def search_menu():
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    frm = ttk.Frame(main_window, padding=10)
    indexing_and_preprocessing()
    frm.grid()
    ttk.Label(frm, text="Θέλω αρχικά να επιλέξεις το μοντέλο με το οποίο θα γίνεται η αναζήτησή σου:").grid(column=0, row=0)
    ttk.OptionMenu(frm, "Επιλογή μοντέλου", "Μοντέλο 1", "Μοντέλο 2", "Μοντέλο 3").grid(column=1, row=2)
    ttk.Label(frm, text="Επιλέξτε μία από τις διαθέσιμες επιλογές του φυλλομετρητή: ").grid(column=0, row=1)
    ttk.Button(frm, text="Έξοδος ", command=main_window.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Αναζήτηση ", command=search_menu).grid(column=1, row=0)
    main_window.mainloop()