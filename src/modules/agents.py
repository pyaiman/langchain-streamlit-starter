from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from src.modules.models import load_chat_model

def sql_agent(message):
    llm = load_chat_model()
    dburi = "sqlite:///src/data/chinook.db" 
    db = SQLDatabase.from_uri(dburi)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)
    response = agent.run(message)
    return response
