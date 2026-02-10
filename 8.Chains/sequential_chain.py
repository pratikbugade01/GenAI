from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1 = PromptTemplate(
    template="Generate 5 detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate 5 pointer summery on from the following text \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

output =  chain.invoke({"topic":"unemployment in india"})

print(output)