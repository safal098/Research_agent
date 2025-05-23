from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama  # Updated import
from textwrap import dedent

# Initialize Ollama with your preferred model
ollama = Ollama(
    model="ollama/deepseek-r1:7b",  # Add 'ollama/' prefix
    base_url="http://localhost:11434"
)

# Define your agents with Ollama
researcher = Agent(
    role='Research Analyst',
    goal='Conduct comprehensive research on given topics',
    backstory=dedent('''...
    '''),
    llm='ollama/deepseek-r1:7b',  # Add 'ollama/' prefix
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Create engaging and informative content based on research',
    backstory=dedent('''
        You are a skilled content writer with expertise in converting
        complex information into clear, engaging, and reader-friendly content.
        You excel at maintaining a consistent tone and style.'''),
    llm=ollama  # Use Ollama here
)

# Define your tasks
research_task = Task(
    description=dedent('''
        Research the latest developments in artificial intelligence
        and its impact on the job market. Focus on:
        1. Recent breakthroughs in AI
        2. Industries most affected
        3. New job opportunities created
        4. Skills needed for the future'''),
    expected_output=dedent('''
        A comprehensive research report covering:
        - Latest AI developments and breakthroughs
        - Analysis of affected industries
        - Emerging job opportunities
        - Future skill requirements'''),
    agent=researcher
)

writing_task = Task(
    description=dedent('''
        Create a comprehensive blog post about AI and the future of work.
        Use the research provided to create an engaging article that:
        1. Explains the current state of AI
        2. Discusses its impact on jobs
        3. Provides actionable advice for professionals
        4. Maintains an optimistic yet realistic tone'''),
    expected_output=dedent('''
        A well-structured blog post that:
        - Summarizes current AI developments
        - Explains job market impacts
        - Provides practical advice
        - Maintains engaging tone'''),
    agent=writer
)

# Create your crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True,
    model='ollama/deepseek-r1:7b'  # Add 'ollama/' prefix
)

# Get your crew to work!
result = crew.kickoff()

# Print the result
print("\nCrew's Report:")
print(result)