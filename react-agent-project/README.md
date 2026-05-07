# Beginner-Friendly Python ReAct Agent

## Introduction
Welcome to the beginner-friendly Python ReAct Agent project! This project demonstrates how an Artificial Intelligence agent can use the **ReAct (Reasoning and Acting)** framework to solve problems step-by-step using tools. It is built entirely with basic Python and requires no external libraries or paid APIs.

## What is a ReAct Agent?
ReAct is a powerful paradigm in AI where an agent interleaves **Reasoning** (thinking about the problem) with **Acting** (using tools to gather information). This combination allows the agent to handle complex tasks by breaking them down into logical steps, observing the real-world results of its actions, and adapting its plan accordingly to arrive at a final answer.

## Folder Structure
```
react-agent-project/
│
├── src/
│   └── react_agent.py
│
├── screenshots/
│   └── output.png
│
├── README.md
│
└── requirements.txt
```

## Technologies Used
- **Python 3**: The core programming language used to build the agent.
- **Google Colab**: The recommended environment for running and testing the code easily without local setup.

## How to Run in Google Colab
1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook.
3. Open `src/react_agent.py` from this project and copy its entire contents.
4. Paste the code into a code cell in your Colab notebook.
5. Run the cell by clicking the Play button or pressing `Shift + Enter`.
6. Observe the agent's step-by-step thought process in the output area below the cell.

## Example Input and Output

When you run the script, the agent is presented with the following query:
`"What is 25 * 4?"`

The output will be exactly in this format:
```text
User Query: What is 25 * 4?

Thought: The user is asking for a math calculation.

Action: Use calculator tool

Observation: Calculator returned 100

Final Answer: The answer is 100
```

## Explanation of the ReAct Process
Our agent simulates the core ReAct loop:
- **Thought**: The reasoning phase. The agent analyzes the user's query and logically figures out what needs to be done. It acts as the "brain" of the operation.
- **Action**: The execution phase. Based on its thought process, the agent decides to use a specific tool (in this case, our simple calculator tool function).
- **Observation**: The feedback phase. The agent looks at the result returned by the tool to gather factual information from the environment.
- **Final Answer**: The conclusion. The agent synthesizes the observation into a final, user-friendly response.

## Screenshots
*(After running the code in Google Colab, please take a screenshot of your output and save it as `output.png` inside the `screenshots` folder of your project submission.)*

## Learning Outcomes
By completing this project, you will learn:
- The fundamental concepts behind the ReAct (Reasoning and Acting) framework.
- How AI agents break down complex problems into Thought, Action, and Observation steps.
- How to integrate external tools (like a calculator function) into an agent's workflow.
- How to structure a clean, professional Python project with proper documentation and comments.

## Conclusion
This minimal project serves as a perfect stepping stone into the exciting world of AI agents. By understanding this basic loop of reasoning and acting, you are now prepared to explore more advanced agents that utilize Large Language Models (LLMs) and complex toolchains!
