## Installation and Running of Create AI Project with Multiple Language Models

### Objective:

To install and run the Create AI project allowing switching between multiple large language models, including OpenAI models (GPT-3, GPT-4) and grok models (LLAMA-3, Mixtral, Google's GEMMA), and set up the frontend interface using Streamlit.

### Video Walkthrough:
https://youtu.be/bvKzy6CqpvM

### Key Steps:

1. **Install Required Tools:**

   - Ensure you have VS Code, GIT, PipX, and Poetry installed on your computer. Follow a guide to set up these tools if needed.

2. **Clone GitHub Repository:**

   - Copy the GitHub repository link and use the command `git clone <repository link>` to clone the project.
   - Move into the project folder using `cd <folder name>`.

3. **Install Dependencies:**

   - Run `poetry install --no-root` to install project dependencies.

4. **Set Up API Keys:**

   - Add API keys for OpenAI, Groq, and Serper in the Streamlit_app.py file.
   - Alternatively, create a `.secrets` file with API keys and place it in the specified directory.

5. **Run the Application:**

   - Execute `streamlit run streamlit_app.py` to start the application.
   - Enter search topics or queries to test the application functionality.

6. **Customize Language Models:**

   - Modify the `agents.py` file to change the large language model being used.
   - Update the selected model in the code to switch between available options.

### Cautionary Notes:

- Ensure API keys are correctly entered to avoid errors during execution.
- Limit the number of iterations and tools used with Grok LLMs to prevent crashing due to token limits.
- Monitor token usage to adjust settings and prevent reaching token limits prematurely.

### Tips for Efficiency:

- Keep the number of tools used by agents in check to optimize performance.
- Limit iterations to control costs when using advanced language models like GPT-3 or GPT-4.
- Regularly test the application and adjust settings as needed to maintain smooth operation.

By following these steps, you can effectively install and run the Create AI project with multiple language models and streamline the process of switching between different models for various tasks.
