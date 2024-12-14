# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr
from elasticsearch import Elasticsearch

global client
client = Elasticsearch("https://localhost:9200",basic_auth=("elastic", "PBnfeM70JxtCuo0ki2Xw"),verify_certs=False)

if client.indices.exists(index="last_statement"):
    print("Το ευρετήριο υπάρχει ήδη. Εκκίνηση διαγραφής...")
    resp = client.indices.delete(index="last_statement")

if client.ping():
    print("Επιτυχής σύνδεση στο Elasticsearch!")
else:
    print("Μη επιτυχής σύνδεση στο Elasticsearch.")
