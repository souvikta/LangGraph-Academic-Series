# state.py
import operator
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage, AIMessage, ToolMessage

class AgentState(TypedDict):
    """
    Represents the state of our agent.

    Attributes:
        messages: A list of all messages in the conversation.
        intermediate_steps: A list of action-observation pairs.
    """
    messages: Annotated[List[BaseMessage], operator.add]
    intermediate_steps: Annotated[List[tuple[AIMessage, ToolMessage]], operator.add]