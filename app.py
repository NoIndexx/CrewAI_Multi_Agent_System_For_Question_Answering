import streamlit as st
import warnings
import yaml
import os
import textwrap
from helper import load_env
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from pydantic import BaseModel, Field, SkipValidation
from typing import List
from streamlit.components.v1 import html

# Ignore warnings
warnings.filterwarnings('ignore')

# Load environment variables
load_env()

# Pydantic class for structured output
class QAOutput(BaseModel):
    answer: str = Field(..., description="The answer to the user's question, based on the retrieved information.")
    sources: List[str] = Field(..., description="The sources of information used to answer the question.")

# Function to configure and run the crew
def run_crew(question):
    # Load settings from YAML
    files = {
        'agents': 'agents.yaml',
        'tasks': 'tasks.yaml'
    }
    
    configs = {}
    for config_type, file_path in files.items():
        with open(file_path, 'r') as file:
            configs[config_type] = yaml.safe_load(file)
    
    agents_config = configs['agents']
    tasks_config = configs['tasks']
    
    # Configure the LLM models
    groq_llm = "groq/llama-3.3-70b-versatile"
    
    # Create agents
    information_retrieval_agent = Agent(
        config=agents_config['information_retrieval_agent'],
        tools=[SerperDevTool(), ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=groq_llm,
        verbose=True
    )
    
    answer_generation_agent = Agent(
        config=agents_config['answer_generation_agent'],
        verbose=True
    )
    
    # Create tasks
    retrieve_information_task = Task(
        config=tasks_config['retrieve_information'],
        agent=information_retrieval_agent
    )
    
    generate_answer_task = Task(
        config=tasks_config['generate_answer'],
        agent=answer_generation_agent,
        context=[retrieve_information_task],
        output_pydantic=QAOutput
    )
    
    # Create crew
    qa_crew = Crew(
        agents=[
            information_retrieval_agent,
            answer_generation_agent
        ],
        tasks=[
            retrieve_information_task,
            generate_answer_task
        ],
        verbose=True
    )
    
    # Run the crew
    return qa_crew.kickoff(inputs={
        'question': question
    })

# Streamlit interface
st.title("AI Question Answering System")
st.write("Ask any question and get a concise, context-aware answer powered by AI.")

# Input field for the question
st.write("Insert your question here:")
question = st.text_input(label="Question Input", value="What is the latest news regarding the Pope?", label_visibility="collapsed")

# Variable to store the result
result = None

# Run button
if st.button("Get Answer", use_container_width=True):
    if not question:
        st.error("Please enter a question.")
    else:
        with st.spinner("Finding an answer... This may take a few minutes."):
            try:
                # Display a message to let the user know the process has started
                progress_placeholder = st.empty()
                progress_placeholder.info("The agents are working! You'll see updates in the terminal as they work.")
                
                # Run the crew
                result = run_crew(question)
                
                # Clear the progress message
                progress_placeholder.empty()
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.error("Check if all API keys are configured correctly in the .env file")

# Display content if result exists
if result:
    # Display answer
    st.subheader("Answer")
    st.markdown(result.pydantic.dict()['answer'])
    
    # Display sources
    st.subheader("Sources")
    sources = result.pydantic.dict().get('sources', [])
    if sources:
        for i, source in enumerate(sources):
            st.markdown(f"**Source {i+1}:**")
            st.write(source)
            st.markdown("---")
    else:
        st.info("No sources provided.")
else:
    st.info("Enter a question and click 'Get Answer' to see the result.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Renato Oliveira | CrewAI Multi-Agent System for Question Answering 🤖") 