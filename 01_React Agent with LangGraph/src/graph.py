# graph.py
from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import call_model, tool_node
from edges import should_continue

# Define a new graph
workflow = StateGraph(AgentState)

# Define the nodes
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# Set the entrypoint
workflow.set_entry_point("agent")

# Add the conditional edge
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

# Add the normal edge
workflow.add_edge("tools", "agent")

# Compile the graph
graph = workflow.compile()