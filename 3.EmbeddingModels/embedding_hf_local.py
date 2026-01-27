from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

''' # For 1 query 
text = "Delhi is the capital of India"

vector = embedding.embed_query(text)
'''

#For Document
document = [
    "Delhi is the capital of India",
    "Kolkata is the capital of west bengal",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(document)

print(str(vector))