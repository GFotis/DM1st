# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

#this code is for laptop
from elasticsearch import Elasticsearch
"""
global client
client = Elasticsearch("https://localhost:9200",basic_auth=("elastic", "xAISMeh9AnvmRzjOo9SH"),verify_certs=False)

if client.ping():
    print("Connected to Elasticsearch!")
else:
    print("Could not connect to Elasticsearch.")
"""
from elasticsearch import Elasticsearch

global client
client = Elasticsearch("https://localhost:9200",basic_auth=("elastic", "PBnfeM70JxtCuo0ki2Xw"),verify_certs=False)

resp = client.indices.delete(
    index="last_statement",
)

if client.ping():
    print("Connected to Elasticsearch!")
else:
    print("Could not connect to Elasticsearch.")
