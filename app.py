import streamlit as st
import subprocess

st.title("⚽ World Cup 2026 Prediction Model")

st.write("Enter two teams (must match dataset names exactly)")

team1 = st.text_input("Team A (e.g. brazil)")
team2 = st.text_input("Team B (e.g. argentina)")

if st.button("Predict Match"):

    if not team1 or not team2:
        st.error("Enter both teams")
    else:
        try:
            result = subprocess.run(
                ["node", "predict.mjs", team1.lower(), team2.lower()],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                st.error("Model error")
                st.text(result.stderr)
            else:
                st.subheader("Prediction Output")
                st.text(result.stdout)

        except FileNotFoundError:
            st.error("Node.js is not available in this environment.")
            st.info("This repo requires Node runtime (not Streamlit Python runtime).")
