from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f" Based {inputs} figure out what it is that the user needs in order to figure out their problem, check https://www.thetoolbus.ai/ai-tools, and https://appsumo.com/collections/new/ for relevant tools that could be usefull ",
          expected_output=f"A clear explanation of the principles, concepts, disciplines, and skills needed by the visionary in order to accomoplish their goal"

      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description=f"Evaluate the following report: {context}. Based on the results, create a learning plan, figure out the things the user needs to learn and focus on.",
        expected_output=f"A thorough learning plan for the next agent"
   
    )


    def writing_task(self, agent, context, inputs):
        return Task(
            agent=agent,
            context=context,
            description=f"Answer the users inquiry their request topics: {inputs} Given the following learning plan {context}, using web search, web scraping ,figure give 5 principles or concepts that the user needs to learn with a short overview of each one and what it is, 5 internet articles titles and their URL, 5 books name and author and their purpose.",
            expected_output=f" 5 principles and concepts reviewed, and thoroughly explaiened , 5 internet articles titles and their URL,  5 books name and author and their purpose.",
        )




