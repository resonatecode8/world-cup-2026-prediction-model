import streamlit as st
from model import match_prob

st.title("⚽ Match Predictor")

TEAM_ELO = {
    "brazil": 2100,
    "france": 2080,
    "argentina": 2075,
    "england": 2050,
    "germany": 2030,
    "spain": 2025,
    "portugal": 2015,
    "netherlands": 2005
}

team1 = st.selectbox("Team 1", list(TEAM_ELO.keys()))
team2 = st.selectbox("Team 2", list(TEAM_ELO.keys()))

if st.button("Predict Match"):

    a = TEAM_ELO[team1]
    b = TEAM_ELO[team2]

    result = match_prob(a, b)

    st.subheader(f"{team1.title()} vs {team2.title()}")

    st.write("Win A:", round(result["winA"] * 100, 2), "%")
    st.write("Draw:", round(result["draw"] * 100, 2), "%")
    st.write("Win B:", round(result["winB"] * 100, 2), "%")

    st.write("Expected Goals A:", round(result["expectedGoalsA"], 2))
    st.write("Expected Goals B:", round(result["expectedGoalsB"], 2))
