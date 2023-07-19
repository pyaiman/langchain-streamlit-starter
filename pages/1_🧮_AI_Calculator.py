import streamlit as st
from src.components.sidebar import sidebar
from src.modules.chains import math_chain
from src.components.chat import display_chat

def main():
    st.set_page_config(page_title="AI Calculator", page_icon="🧮")
    sidebar()
    st.header('🧮 AI Calculator')
    display_chat(math_chain)

if __name__ == "__main__":
    main()
