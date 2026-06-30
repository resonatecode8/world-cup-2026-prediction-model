import streamlit as st
import subprocess

st.title("⚽ World Cup 2026 Prediction Model")

# 🔥 SAFE STATIC TEAM LIST (from World Cup 2026 dataset)
TEAMS = [
    "brazil","france","argentina","germany","spain","portugal",
    "england","netherlands","italy","belgium","croatia","uruguay",
    "mexico","usa","japan","south korea","morocco","senegal",
    "switzerland","denmark","colombia","chile","ecuador","australia"
]

team1 = st.selectbox("Team A", TEAMS)
team2 = st.selectbox("Team B", TEAMS)

if st.button("Predict Match"):

    result = subprocess.run(
        ["node", "predict.mjs", team1, team2],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        st.error("Prediction failed")
        st.text(result.stderr)
    else:
        st.subheader("Prediction Output")
        st.text(result.stdout)
