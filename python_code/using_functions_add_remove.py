# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr
from elasticsearch_connection import client
import json
from add_remove import add_from_file
from add_remove import remove_from_index
import os
#while True:
#    file_path=input("Give me the csv path:")
#    if os.path.exists(file_path):
#        print(f"The file '{file_path}' exists.")
#        add_from_file(file_path)
#        break
#    else:
#        print(f"The file '{file_path}' does not exist.")

docs_to_remove=input("Please input doc_ids to remove(separated by space):").split()
docs_to_remove = [docs for docs in docs_to_remove]
for doc_ids in docs_to_remove:
    remove_from_index(doc_ids)

