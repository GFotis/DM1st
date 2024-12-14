# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

import tkinter as tk
from tkinter import ttk
from search import search_menu
from add_remove import addremove_menu

def first_menu():
    #main_window.destroy()
    search_menu()

def second_menu():
    #main_window.destroy()
    addremove_menu()

def main_menu():
    main_window = tk.Tk()
    main_window.title("Browser \"The Incognitooo...\"")
    main_window.geometry("1366x768")  # Width x Height
    frm = ttk.Frame(main_window, padding=10)
    frm.pack()
    ttk.Label(frm, text="Καλώς ήρθες στον φυλλομετρητή μας!", background="lightblue").pack(anchor="center")
    ttk.Label(frm, text="Είσαι τόσο incognito όπως ο Batman!", background="lightblue").pack(anchor="center")
    ttk.Label(frm, text="").pack(anchor="center")
    ttk.Label(frm, text="Επέλεξε μία από τις διαθέσιμες επιλογές του φυλλομετρητή: ", background="lightblue").pack(anchor="center")
    ttk.Button(frm, text="Αναζήτηση", command=first_menu).pack(anchor="center")
    ttk.Button(frm, text="Προσθήκη/Αφαίρεση από τη βάση πληροφορίας", command=second_menu).pack(anchor="center")
    ttk.Button(frm, text="Έξοδος", command=main_window.destroy).pack(anchor="center")
    main_window.mainloop()