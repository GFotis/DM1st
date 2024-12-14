# Omada ekponishs ergasias:
# Fotios Galanis 2022202000032 dit20032@go.uop.gr
# Dimitrios Bozikakis 2022202000027 dit20027@go.uop.gr

from sentence_transformers import SentenceTransformer

def knn(query,k_size):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query = "What is Elasticsearch k-NN search?"
    query_vector = model.encode(query).tolist()
   # {'query': {'bool': {'must': [{'match': {'LastName': 'Autry'}}, {'match': {'FirstName': 'James'}}], 'should': [], 'must_not': []}}}
    query = {
        "size": k_size,  # MAS TO DINEI O XRHSTHS
        "query": {
            "script_score": {
                "query": {"match_all": {}},  # Use a filter if needed
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'Last_Statement') + 1.0",  
                    "params": {"query_vector": query_vector}
                }
            }
        }
    }
    return query