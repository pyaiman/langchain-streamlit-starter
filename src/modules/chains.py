from langchain import LLMMathChain
from src.modules.models import load_chat_model

def math_chain(query):
    llm = load_chat_model()
    llm_math = LLMMathChain.from_llm(llm, verbose=True)
    response = llm_math.run(query)
    return response