from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import datetime

# Example tool function
def get_time(params):
    return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

# Define tools
tools = [
    Tool.from_function(
        name="get_time",
        description="Get current time",
        func=lambda _: get_time({}),
    )
]

# Initialize local LLM (Ollama)
llm = Ollama(model="llama3")  # Make sure to run: `ollama run llama3`

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def handle_mcp_action(action, params):
    prompt = f"Action: {action}, Params: {params}. Perform the action."
    result = agent.run(prompt)
    return result
