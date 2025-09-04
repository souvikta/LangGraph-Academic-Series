import os
from dotenv import load_dotenv
from IPython.display import Image, display
load_dotenv()

import asyncio
from typing import AsyncIterator
from langchain_core.messages import BaseMessage,AIMessage


from graph import graph


async def stream_final_answer(stream: AsyncIterator):
    """Helper function to stream only the final AIMessage tokens."""
    # The 'astream_events' method streams all graph events
    # We filter for the final response event from the 'agent' node
    async for event in stream:
        if event["event"] == "on_chat_model_stream":
            chunk = event["data"]["chunk"]
            if isinstance(chunk, AIMessage):
                print(chunk.content, end="", flush=True)


def main():
    """Main function to run the ReAct agent."""
    # ... (your graph display code) ...

    inputs = {"messages": [("user", "Who is the director of the movie 'Breathless', and what is the current time in their city of birth?")],
              "intermediate_steps": [],}
    
    # We use asyncio.run to execute our async streaming function
    print("Final Answer: ", end="", flush=True)
    asyncio.run(stream_final_answer(graph.astream_events(inputs, version="v1")))
    print() # For a final newline

if __name__ == "__main__":
    main()