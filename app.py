import streamlit as st
import numpy as np

presets = {
    "Easy": [[1, 2, 3], [4, 5, 6], [7, 0, 8]],
    "Medium": [[2, 8, 3], [1, 6, 4], [7, 0, 5]],
    "Hard": [[8, 6, 7], [2, 5, 4], [3, 0, 1]],
    "Goal": [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
}

st.title("🧩 8-Puzzle Solver")

start_key = st.selectbox("Select Start State", list(presets.keys()))
goal_key = st.selectbox("Select Goal State", list(presets.keys()))

start_state = presets[start_key]
goal_state = presets[goal_key]

st.write("### Start State:")
st.table(np.array(start_state))

st.write("### Goal State:")
st.table(np.array(goal_state))
