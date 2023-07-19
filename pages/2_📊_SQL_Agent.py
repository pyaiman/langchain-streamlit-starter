import streamlit as st
from src.components.sidebar import sidebar
from src.modules.agents import sql_agent
from src.components.chat import display_chat

def main():
    st.set_page_config(page_title="SQL Agent", page_icon="📊")
    sidebar()
    st.header('📊 SQL Agent')
    display_chat(sql_agent)

if __name__ == "__main__":
    main()
