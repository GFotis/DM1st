# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

#ElasticSearch: localhost:9200
#Kibana: localhost:5601
#Username: elastic
#Password: PBnfeM70JxtCuo0ki2Xw

import tkinter as tk # Dictionary for the GUI application
from preproccess_phase import indexing

indexing.create_index()

# GUI
root = tk.Tk()
root.title("My GUI Application")
root.geometry("1366x768")  # Width x Height
root.mainloop()
