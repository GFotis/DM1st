# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

#ElasticSearch: localhost:9200
#Kibana: localhost:5601
#Username: elastic
#Password: PBnfeM70JxtCuo0ki2Xw

from elasticsearch import Elasticsearch
#import pandas as pd # vivliothiki gia diaxeirisi dedomenon
import tkinter as tk # vivliothiki gia dimiourgia gui

# Connect to the elasticsearch cluster
#es = Elasticsearch("https://localhost:9200",basic_auth=("elastic", "PBnfeM70JxtCuo0ki2Xw"),verify_certs=False)

#if es.ping():
#    print("Connected to Elasticsearch!")
#else:
#    print("Could not connect to Elasticsearch.")


# Initialize index dictionary
index = {}

# Open the data file
with open('input_data\\Texas Last Statement.csv', 'r') as file:
    # Skip the first line (header)
    next(file)
    
    # Process each line
    for row_number, line in enumerate(file, start=1):
        last_column = line.split(',')[-1].strip()
        words = last_column.split()
        
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(row_number)

# Print the index (for debugging purposes)
for word, rows in index.items():
    print(f"{word}: {rows}")

# GUI
root = tk.Tk()
root.title("My GUI Application")
root.geometry("1366x768")  # Width x Height
root.mainloop()
