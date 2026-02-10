from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal["positive","negative"] = Field(description="Give the sentiment of the feedback")

p_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="classify the sentiment of the following feedback text into positive or negetive \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":p_parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | p_parser

prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model | parser),
    (lambda x:x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback":"This is a beautiful phone"})

print(result)