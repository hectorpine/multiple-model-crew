import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os

st.title('Your Research Assistant')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter Research Details')
    topic = st.text_input("Main topic of your research:")
    detailed_questions = st.text_area("Specific questions or subtopics you are interested in exploring:")

if st.button('Run Research'):
    if not topic or not detailed_questions:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Research Topic: {topic}\nDetailed Questions: {detailed_questions}"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Results of your research project:")
        st.write(result)
