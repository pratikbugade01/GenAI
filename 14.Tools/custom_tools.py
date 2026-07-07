from langchain_community.tools import tool

@tool
def multiply(a, b):
    """Multiply two numbers"""
    return a*b

result = multiply.invoke(10,50)

print(result)