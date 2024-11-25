from elasticsearch import Elasticsearch
import pandas as pd # vivliothiki gia diaxeirisi dedomenon
import tkinter as tk # vivliothiki gia dimiourgia gui

# Connect to the elasticsearch cluster
es = Elasticsearch("https://localhost:9200",basic_auth=("elastic", "PBnfeM70JxtCuo0ki2Xw"),verify_certs=False)

if es.ping():
    print("Connected to Elasticsearch!")
else:
    print("Could not connect to Elasticsearch.")

# GUI
root = tk.Tk()
root.title("My GUI Application")
root.geometry("1366x768")  # Width x Height
root.mainloop()
