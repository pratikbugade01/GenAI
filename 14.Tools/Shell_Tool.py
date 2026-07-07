from langchain_community import tools

shell_tool = tools.ShellTool()

result = shell_tool.invoke("ls")

print(result)