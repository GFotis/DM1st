# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk # Dictionary for the GUI application
from tkinter import ttk # Dictionary for the GUI application
#from add_remove import addremove_menu
from search import search_menu
from add_remove import addremove_menu
 
# GUI
def first_menu():
    main_window.destroy()
    search_menu()

def second_menu():
    main_window.destroy()
    addremove_menu()

def main_menu():
    global main_window
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    frm = ttk.Frame(main_window, padding=10)
    frm.pack()
    ttk.Label(frm, text="Καλώς ήρθες στον φυλλομετρητή μας!").pack(anchor="center")
    ttk.Label(frm, text="Είσαι τόσο incognito όπως ο Batman!").pack(anchor="center")
    #ttk.Label(frm, text="Δημιούργησε τον δικό σου φυλλομετρητή μεταμορφώνοντας το αρχείο από το οποίο θα ανακτώνται οι πληροφορίες:").pack(anchor="center")
    #import_button = tk.Button(main_window, text=&quot;Import File&quot;, command=import_file)
    #import_button.pack(pady=100)
    ttk.Label(frm, text="Αρχικά θα ήθελα να ανεβάσεις το αρχείο από το οποίο  ").pack(anchor="center")
    ttk.Label(frm, text="ΕΕφόσον το ανεβάσεις. επέλεξε μία από τις διαθέσιμες επιλογές του φυλλομετρητή: ").pack(anchor="center")
    ttk.Button(frm, text="Αναζήτηση", command=first_menu).pack(anchor="center")
    ttk.Button(frm, text="Προσθήκη/Αφαίρεση από τη βάση πληροφορίας", command=second_menu).pack(anchor="center")
    ttk.Button(frm, text="Έξοδος", command=main_window.destroy).pack(anchor="center")
    #ttk.Button(frm, text="Προσθήκη/Διαγραφή καταχώρησης", command=addremove_menu).grid(column=1, row=2)
    main_window.mainloop()