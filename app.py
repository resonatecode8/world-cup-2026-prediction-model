import streamlit as st
import json

st.title("⚽ World Cup 2026 Prediction Model")

# Load data safely (handles real repo structure)
@st.cache_data
def load_teams():
    with open("data/elo-calibrated.json", "r") as f:
        data = json.load(f)

    teams = {}

    # CASE 1: list format (most likely your repo)
    if isinstance(data, list):
        for item in data:
            name = item.get("team") or item.get("name")
            rating = item.get("elo") or item.get("rating") or item.get("ratings")

            if name and rating:
                teams[name] = float(rating)

    # CASE 2: dict format
    elif isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (int, float)):
                teams[k] = v

    return teams


TEAM_ELO = load_teams()

if not TEAM_ELO:
    st.error("Could not load team ratings. Check JSON format.")
    st.stop()


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


teams = sorted(TEAM_ELO.keys())

st.subheader("Select Match")

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
