from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/Lenovo-i9-12900HX-40-64cm-500Nits-82TD009KIN/dp/B0BR4BX2F8/ref=sr_1_13?crid=29I1Y6Z8XQDUV&dib=eyJ2IjoiMSJ9.mlONKszMsrgW1Q-3DJTFxGo36zdR1W6_Rka8LYnt8BHn_l-enlw9RIEdFUM4ZqUCpyw8KS4TgVM5cjEv6IDzw0C10f6KYxujU5sMjZ4ha92K-xbyokf3PgHvFtud6e8wKRhSmLXAsdNRRqBBpNffEcso5QWmTfLyqOxEJ8sL8lnkXv2pzQ1y87faTBYI6q-BKWIhvH6ANwb6pz8GgtnYhcnvfm89XRQYoKa_PYF3eRE.xpPLF_PrxO8lWDXdNmXePcy8-Ba011FZswhAaTv3uM0&dib_tag=se&keywords=lenovo+legion+laptop&qid=1772963206&sprefix=lenovo+legin%2Caps%2C401&sr=8-13'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))