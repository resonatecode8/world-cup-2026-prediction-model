import streamlit as st
import json

st.title("⚽ World Cup 2026 Prediction Model")

# Load Elo ratings
@st.cache_data
def load_teams():
    with open("data/elo-calibrated.json", "r") as f:
        data = json.load(f)

    # handle both formats: dict OR list
    if isinstance(data, dict):
        return data

    if isinstance(data, list):
        return {t["team"].lower(): t["elo"] for t in data}

    return {}

TEAM_ELO = load_teams()

if not TEAM_ELO:
    st.error("No team data found. Check data/elo-calibrated.json")
    st.stop()

# Simple Elo → goal model (Dixon-Coles simplified)
def expected_goals(diff):
    return max(0.3, min(3.5, 1.35 + diff / 400))

def match_prob(a, b):
    goal_a = expected_goals(a - b)
    goal_b = expected_goals(b - a)

    total = goal_a + goal_b

    win_a = goal_a / total
    win_b = goal_b / total
    draw = 1 - (win_a + win_b)

    return win_a, draw, win_b, goal_a, goal_b


st.subheader("Select Match")

teams = sorted(TEAM_ELO.keys())

team1 = st.selectbox("Team A", teams)
team2 = st.selectbox("Team B", teams)

if st.button("Predict Match"):

    a = TEAM_ELO[team1]
    b = TEAM_ELO[team2]

    win_a, draw, win_b, ga, gb = match_prob(a, b)

    st.subheader("Result Probabilities")

    st.write(f"**{team1} win:** {win_a:.2%}")
    st.write(f"**Draw:** {draw:.2%}")
    st.write(f"**{team2} win:** {win_b:.2%}")

    st.subheader("Expected Goals")
    st.write(f"{team1}: {ga:.2f}")
    st.write(f"{team2}: {gb:.2f}")
