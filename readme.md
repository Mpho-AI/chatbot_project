To run the chatbot locally:

1. Clone the repository: `git clone https://github.com/your-username/chatbot-backend.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Django server: `python manage.py runserver`
4. Open a web browser and navigate to `http://localhost:8000/api/response/?input=What+is+the+poverty+rate+in+Brazil?`

Problem description:

Objective: Build a chatbot backend using Django and Python that integrates a Retrieval-Augmented Generation (RAG) model as well as a small or large language model, leveraging the three provided data sources for responses. Additionally, implement an API endpoint to connect with any frontend application.

Instructions
Create a new Django project with necessary configurations and app structure for the chatbot.
Implement the chatbot logic within the Django app, using RAG for response generation. 
Integrate the three provided data sources about Brazil. These data sources are specified below:
Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population) - World, Brazil [https://data.worldbank.org/indicator/SI.POV.DDAY?locations=1W-BR]
Individuals using the Internet (% of population) - World, Brazil [https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W-BR]
Unemployment, total (% of total labor force) (modeled ILO estimate) - World, Brazil [https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=1W-BR]
Incorporate any SLM or LLM for text generation.
Create an API endpoint within Django, that is able to connect to any frontend.
Implement request handling to accept user input and return chatbot responses using JSON
Include a test case to ensure the chatbot functions correctly
Ensure your code is well-organised, follows best practices, and is easy to understand. Use clear and concise variable/function names.
Implement error handling for potential issues like network errors, failed API calls, etc.
Include comments to explain the logic of the chatbot or important decisions in your code.
Provide a README.md file in your repository with clear instructions on how to run the chatbot locally.
Push your code to a Github repository and share the repo with us :)

Assessment Criteria
Code quality: We'll evaluate the clarity, readability, and structure of your code.
Speed: We'll consider the time it takes from confirming the test instructions to submitting the completed test, as well as the time it takes between us sending out this email and you confirming the test instructions.
Functionality: Ensure all specified features work as intended.
Error handling: Assess how well you handle potential issues within your application.
