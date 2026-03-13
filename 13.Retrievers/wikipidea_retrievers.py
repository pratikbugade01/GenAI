from langchain_community.retrievers import WikipediaRetriever
from langchain_core.runnables import RunnableLambda

retriever = WikipediaRetriever(top_k_results=2,lang="en")

query = "What is India"


def print_docs(docs):

    for i,doc in enumerate(docs):
        print(f"\n----- Result {i+1} -----")
        print(f"Content:\n{doc.page_content}...")

chain = retriever | RunnableLambda(print_docs)

chain.invoke(query)