from crewai import Agent
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq  # Import Groq client
from langchain_openai import ChatOpenAI
import os
from crewai_tools import SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool 



class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape=ScrapeWebsiteTool()


       # OpenAI Models
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)
        self.gpt3_5_turbo_0125 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.gpt3_5_turbo_1106 = ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0.7)
        self.gpt3_5_turbo_instruct = ChatOpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)
        
        # Groq Models
        self.llama3_8b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-8b-8192")
        self.llama3_70b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-70b-8192")
        self.mixtral_8x7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="mixtral-8x7b-32768")
        self.gemma_7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="gemma-7b-it")
        
        # CHANGE YOUR MODEL HERE
        self.selected_llm = self.gpt4
    def researcher(self):
    # Detailed agent setup for the Research Expert
        return Agent(
        role='Expert',
        goal='To break down broad visionary ideas into specific, actionable research topics, identify key areas requiring in-depth investigation, and prepare report that serves as a roadmap for future goals.',
        backstory="You are an expert that can easily reconvey ideas from others through critical thinking and systems thinking to figure out what the visionary wants to accompolish",
        verbose=True,
        allow_delegation=False,
        llm=self.selected_llm,
        max_iter=3,
        tools=[self.serper, self.web, self.web_scrape],
        ) 


    def analyst(self):
        # Detailed agent setup for the Analyst
        return Agent(
            role='Analyst',
            goal='Come up with a learning curriculumn that will allow for the visionary to reach deep and broad knowledge in order to accomplish their goals',
            backstory="You are a talented organized logical educator who can deductively comeup with amazing learning plans in order to provide guidance starting from the goal and working backwards to the begining of a novice level so as to easily bridge the gap between inexperienced and experts alike.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3,


        )

    def writer(self):
        # Detailed agent setup for the Writer
        return Agent(
            role='Technical writer',
            goal='Use CrewAI tools to search and summarize findings of the previous agent, internet articles titles and their URLs, as well as books and online resource to carry out the learning needed',
            backstory="You are organized course creater and talented educator that understands what it takes for beginners to get from point a to point be when it comes to learning, you export great findings, you are great at scraping the web links and resources geared to ward learning specific goals.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web, self.web_scrape],
            max_iter=3,


        )