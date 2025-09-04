# nodes.py
import json
from langchain_core.messages import ToolMessage, SystemMessage,AIMessage
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI

from state import AgentState
from tools import tools, tools_by_name

# Initialize the model and bind the tools
model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)

def call_model(state: AgentState, config: RunnableConfig):
    """
    The 'agent' node. Invokes the model to decide the next action.
    """
    system_prompt = SystemMessage(
        "You are a helpful AI assistant, please respond to the users query to the best of your ability!"
    )
    response = model.invoke([system_prompt] + state["messages"], config)
    return {"messages": [response]}

def tool_node(state: AgentState):
    """
    The 'tools' node. Executes tools and records the action-observation pair.
    """
    # Get the last message, which is the AI's tool call
    agent_action = state["messages"][-1]
    
    outputs = []
    for tool_call in agent_action.tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
        
    # We now return both the new ToolMessages and the intermediate step
    return {
        "messages": outputs,
        "intermediate_steps": [(agent_action, outputs[0])], # Storing the pair
    }
