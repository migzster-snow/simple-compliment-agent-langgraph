from typing import Dict, TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    message: str


def compliment_node(state: AgentState) -> AgentState:
    state["message"] = f"{state['message']}, you are doing an amazing job!"
    return state


graph = StateGraph(AgentState)
graph.add_node("complimenter", compliment_node)
graph.set_entry_point("complimenter")
graph.set_finish_point("complimenter")

app = graph.compile()

result = app.invoke({"message": "Jonah"})
print("Result: ", result["message"])
