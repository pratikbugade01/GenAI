from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='10.Document_Loaders\CSV_loader\laptop_data.csv')

docs = loader.load()

print(len(docs))
print(docs[1])