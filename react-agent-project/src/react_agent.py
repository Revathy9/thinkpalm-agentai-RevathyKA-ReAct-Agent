"""
A minimal, beginner-friendly ReAct (Reasoning and Acting) Agent in Python.

What is ReAct?
ReAct is a paradigm where an AI agent combines "Reasoning" (thinking about what to do)
and "Acting" (using tools to achieve a goal). It helps the agent break down complex 
problems into manageable steps.
"""

def calculator_tool(expression: str) -> int:
    """
    A simple calculator tool that evaluates basic mathematical expressions.
    
    What the tool does:
    It takes a math expression as a string (e.g., '25 * 4') and returns the calculated result.
    In a real-world scenario, tools are how an agent interacts with the outside world 
    (like searching the web, querying a database, or doing complex math).
    """
    # Note: eval() is used here for simplicity in a beginner project.
    # For production applications, always use a safer math parser.
    return eval(expression)

def react_agent(query: str):
    """
    A minimal ReAct Agent that simulates the Thought, Action, Observation loop.
    
    Why are reasoning and acting combined?
    By reasoning first (Thought), the agent plans its next move logically.
    By acting (Action), it interacts with tools to gather real-world facts (Observation).
    Combining them allows the agent to reliably solve problems it couldn't solve alone.
    """
    print(f"User Query: {query}\n")
    
    # Step 1: Thought
    # The agent thinks about what it needs to do to answer the user's query.
    print("Thought: The user is asking for a math calculation.\n")
    
    # Step 2: Action
    # The agent decides which tool to use.
    print("Action: Use calculator tool\n")
    
    # Extracting the math expression from the query
    # A real LLM would dynamically extract this. We simulate it here for simplicity.
    expression = query.replace("What is ", "").replace("?", "").strip()
    
    # Step 3: Observation
    # The agent uses the tool and observes the result.
    result = calculator_tool(expression)
    print(f"Observation: Calculator returned {result}\n")
    
    # Step 4: Final Answer
    # The agent uses the observation to provide the final answer to the user.
    print(f"Final Answer: The answer is {result}")

if __name__ == "__main__":
    # Example execution
    sample_query = "What is 25 * 4?"
    react_agent(sample_query)
