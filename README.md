🧠 AI Research & Content Writing Crew
A simple but powerful example of using CrewAI with Ollama to create an autonomous agent-based system that performs research on AI and writes content about its impact on the job market.

This project demonstrates how you can build a mini-research-and-content pipeline using LLMs locally via Ollama and CrewAI’s multi-agent framework.

🔧 Features
Autonomous research + writing workflow
Uses local LLMs via Ollama
Modular structure with CrewAI agents
Easy to extend for other topics or use cases
📦 Requirements
Before running this script, ensure you have:

Python 3.9+
crewai
langchain_community
ollama (running locally)
Install dependencies:

bash


1
pip install crewai langchain_community ollama
Note: Make sure the model used (ollama/deepseek-r1:7b) is pulled and available in your local Ollama instance. 

⚙️ Setup Instructions
1. Start Ollama Server
Make sure Ollama is running locally:

bash


1
ollama serve
Pull the required model:

bash


1
ollama pull deepseek-r1:7b
2. Run the Script
Save the provided script as main.py, then run:

bash


1
python main.py
🧪 What It Does
Research Analyst Agent
Researches recent developments in AI and their impact on jobs.
Outputs a structured research summary.
Content Writer Agent
Takes the research output and crafts an engaging blog post.
Maintains clarity, tone, and relevance for readers.
Crew Workflow
Orchestrates both agents sequentially.
Returns a final report ready for publishing or further processing.
🧩 Customization Ideas
You can easily adapt this project for various purposes:

Change the topic of research (e.g., climate change, crypto, robotics)
Add more agents (e.g., editor, fact-checker)
Export output to Markdown or HTML
Integrate into a web app or automation pipeline
📝 License
MIT License – see LICENSE for details.
