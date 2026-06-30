import streamlit as st
from model import match_prob

st.title("⚽ Match Predictor")

team1 = st.text_input("Team 1 rating (e.g. 2000)")
team2 = st.text_input("Team 2 rating (e.g. 1950)")

if st.button("Predict"):

    a = float(team1)
    b = float(team2)

    result = match_prob(a, b)

    st.write("Win A:", round(result["winA"] * 100, 2), "%")
    st.write("Draw:", round(result["draw"] * 100, 2), "%")
    st.write("Win B:", round(result["winB"] * 100, 2), "%")
