import os
from crewai import Agent, Task, Crew, LLM

# 1. Initialize the ultra-fast, free Groq LLM
# We use Llama 3.3 70B because of its elite coding and reasoning performance
groq_llm = LLM(model="groq/llama-3.3-70b-versatile")

# --- 2. Define the Agents ---

reviewer = Agent(
    role="Senior Security & Code Reviewer",
    goal="Analyze the provided Python code to identify potential bugs, vulnerabilities, and anti-patterns.",
    backstory="You are a ruthless but helpful Senior Staff Engineer who specializes in Python security and clean code.",
    llm=groq_llm,
    verbose=True
)

tester = Agent(
    role="QA Automation Engineer",
    goal="Write comprehensive pytest unit tests for the provided code, covering extreme edge cases.",
    backstory="You are a meticulous QA engineer who loves breaking code. You think of edge cases no one else considers.",
    llm=groq_llm,
    verbose=True
)

architect = Agent(
    role="Systems Architect",
    goal="Suggest performance optimizations and time/space complexity improvements.",
    backstory="You are an algorithm expert obsessed with Big O notation and maximum execution speed.",
    llm=groq_llm,
    verbose=True
)

# --- 3. Define the Tasks ---

# Simulate reading a file from the repository
# (In a production environment, you would use Python's os/sys modules to read all modified files)
try:
    with open('calculator.py', 'r') as file:
        code_to_analyze = file.read()
except FileNotFoundError:
    code_to_analyze = """
def divide_numbers(a, b):
    return a / b
""" # Fallback code if the file is missing

review_task = Task(
    description=f"Review the following code for bugs (like division by zero) and security flaws:\n\n{code_to_analyze}",
    expected_output="A bulleted list of bugs and security vulnerabilities found.",
    agent=reviewer
)

test_task = Task(
    description="Based on the code provided in the review task, generate exactly 3 pytest unit tests targeting edge cases.",
    expected_output="A Markdown Python code block containing functional pytest functions.",
    agent=tester
)

optimize_task = Task(
    description="Analyze the code and suggest algorithmic improvements to make it run faster or be more robust. State its current Big O time complexity.",
    expected_output="A markdown report detailing time/space complexity and optimization suggestions.",
    agent=architect
)

# --- 4. Assemble and Run the Crew ---

virtual_team = Crew(
    agents=[reviewer, tester, architect],
    tasks=[review_task, test_task, optimize_task],
    verbose=True
)

# Kick off the workflow!
print("Starting the Virtual Engineering Team analysis...")
result = virtual_team.kickoff()

print("\n==============================================")
print("FINAL AI TEAM REPORT:")
print("==============================================")
print(result.raw)