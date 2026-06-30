import streamlit as st

st.title("World Cup 2026 Prediction Model")

st.write("Welcome to your simulation dashboard")

team = st.text_input("Enter a team")

if st.button("Run Prediction"):
    st.write(f"Running model for: {team}")
