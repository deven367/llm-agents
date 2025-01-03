from langchain_community.tools.shell.tool import ShellTool

shell_tool = ShellTool()

print(shell_tool.run("grv"))