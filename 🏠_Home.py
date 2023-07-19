import streamlit as st
from src.components.welcome_sidebar import welcome_sidebar

def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    welcome_sidebar()
    st.write("# Langchain + Streamlit ⛓️")
    st.write("## 👋 Welcome to the Starter kit")
    st.write("> 🤖 Leveraging the power of LangChain and Language Models (LLM) to explore and experiment various use cases.")
    st.write("##### 📝 We have created an two use case for demo purpose")
    st.write("1. Math Chain [Doc Link](https://python.langchain.com/docs/modules/chains/additional/llm_math)")
    st.write("2. SQL Agent [Doc Link](https://python.langchain.com/docs/modules/agents/toolkits/sql_database)")
    st.markdown("---")
    st.write("## 📚 Resources")
    st.write("> 📖 [Langchain](https://langchain.readthedocs.io/en/latest/)\n")
    st.write("> 📖 [Streamlit](https://python.langchain.com/docs/get_started/introduction.html)")

if __name__ == "__main__":
    main()
