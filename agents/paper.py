from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_anthropic import ChatAnthropic
from langchain_community.agent_toolkits.load_tools import load_tools

llm = ChatAnthropic(
    model="claude-3-sonnet-20240229"
)
tools = load_tools(
    ["arxiv"],
)
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke(
    {
        "input": "What's the paper 1605.08386 about?",
    }
)