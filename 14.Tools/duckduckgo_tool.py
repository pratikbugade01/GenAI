from langchain_community import tools

search_tool = tools.DuckDuckGoSearchResults()
result = search_tool.invoke("today is woman ipl match or worldcoup match?")

print(result,"\n")

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)