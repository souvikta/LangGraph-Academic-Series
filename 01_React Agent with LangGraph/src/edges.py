# edges.py
from state import AgentState

def should_continue(state: AgentState) -> str:
    """
    Determines the next step based on the last message.

    If the last message is a tool call, continue to the 'tools' node.
    Otherwise, end the conversation.
    """
    last_message = state['messages'][-1]
    if last_message.tool_calls:
        return "continue"
    return "end"