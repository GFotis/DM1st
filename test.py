from elasticsearch import Elasticsearch
import pandas as pd
import tkinter as tk

#es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "<PBnfeM70JxtCuo0ki2Xw>"))
es = Elasticsearch(
    "https://localhost:9200",  # or "https://localhost:9200" if HTTPS is enabled
    basic_auth=("elastic", "PBnfeM70JxtCuo0ki2Xw"),  # Replace <your-password> with the correct password
    verify_certs=False
)

# Test the connection
if es.ping():
    print("Connected to Elasticsearch!")
else:
    print("Could not connect to Elasticsearch.")

# Create the main application window
root = tk.Tk()
root.title("My GUI Application")
root.geometry("1366x768")  # Width x Height

# Run the Tkinter event loop
root.mainloop()
