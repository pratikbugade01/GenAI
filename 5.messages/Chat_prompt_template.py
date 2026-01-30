from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a Professional {domain} engineer'),
    ('human','Explain in simple terms,what is {topic}')
])

prompt = chat_template.invoke({'domain':'AIML','topic':'AI'})

print(prompt)