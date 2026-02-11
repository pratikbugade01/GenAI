from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
) 

parser = StrOutputParser()

chain = RunnableParallel({
    "tweet" : RunnableSequence(prompt1,model,parser),
    "linkedin" : RunnableSequence(prompt2,model,parser)
})

result = chain.invoke({"topic":"GenAI vs AgenticAI"})

print(result["tweet"])
print("\n \n ", result["linkedin"])