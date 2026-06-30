import streamlit as st
import subprocess

st.title("⚽ Match Predictor")

team1 = st.text_input("Team 1 (e.g. brazil)")
team2 = st.text_input("Team 2 (e.g. france)")

if st.button("Predict Winner"):

    result = subprocess.run(
        ["node", "predict.mjs", team1.lower(), team2.lower()],
        capture_output=True,
        text=True
    )

    st.text(result.stdout)
