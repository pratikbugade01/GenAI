from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about virat kohali"

doc_embeddings = embedding.embed_documents(docs)
query_embeddings = embedding.embed_query(query)

score = cosine_similarity([query_embeddings],doc_embeddings)[0]

index,score = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print("similarity score is:", score)