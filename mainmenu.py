# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
#from add_remove import addremove_menu
from search import search_menu
 
# GUI
def main_menu():
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    frm = ttk.Frame(main_window, padding=10)
    frm.grid()
    ttk.Label(frm, text="Καλώς ήρθες στον φυλλομετρητή μας!").grid(column=0, row=0)
    ttk.Label(frm, text="Είσαι τόσο incognito όπως ο Batman! Δημιούργησε τον δικό σου φυλλομετρητή μεταμορφώνοντας το αρχείο από το οποίο θα ανακτώνται οι πληροφορίες: ##DEN EXEI FTIAXTEI AKOMA## ").grid(column=1, row=1)
    #import_button = tk.Button(main_window, text=&quot;Import File&quot;, command=import_file)
    #import_button.pack(pady=100)
    ttk.Label(frm, text="Αρχικά θα ήθελα να ανεβάσεις το αρχείο από το οποίο  ").grid(column=0, row=1)
    ttk.Label(frm, text="ΕΕφόσον το ανεβάσεις. επέλεξε μία από τις διαθέσιμες επιλογές του φυλλομετρητή: ").grid(column=0, row=1)
    ttk.Button(frm, text="Έξοδος", command=main_window.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Αναζήτηση", command=search_menu).grid(column=1, row=1)
    #ttk.Button(frm, text="Προσθήκη/Διαγραφή καταχώρησης", command=addremove_menu).grid(column=1, row=2)
    main_window.mainloop()