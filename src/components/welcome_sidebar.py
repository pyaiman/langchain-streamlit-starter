import streamlit as st

def welcome_sidebar():
    with st.sidebar:
        st.image("src/assets/gpt-wizard.png")
        st.markdown(
            "🧙‍♂️✨ Welcome to the [GPT Wizards](https://github.com/GPT-Wizard) community! 🌟 We're a group of technologists and AI enthusiasts who are passionately exploring the incredible capabilities of OpenAI's GPT. Join us as we push the boundaries and develop innovative applications using this powerful tool. 🚀 Let's embark on this exciting journey together! 🌌"
        )
        st.markdown("---")
        st.image("src/assets/tw-logo.png")