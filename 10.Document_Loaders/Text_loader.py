from langchain_community.document_loaders.text import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")


prompt = PromptTemplate(
    template= "Write a summary for the following poem - \n {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader('10.Document_Loaders\cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs[0].page_content,"\n \n")

print(docs[0].metadata)

chain = prompt | model | parser

print("\n \n",chain.invoke({'poem':docs[0].page_content}))

