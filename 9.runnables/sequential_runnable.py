from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="write a job about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
) 

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({"topic":"AI"}))