from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {topic}',
    input_variables=['topic']
) 

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_Chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "explanation" : RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_Chain)

result = final_chain.invoke({"topic":"cricket"})

print(result["joke"])
print("\n \n ", result["explanation"])