import streamlit as st
import time
import numpy as np
import rsi_converted as dt

st.write("""
# Simple Stock Predictor App
""")

st.markdown("Language: Python")
st.markdown("Technologies: :")
st.markdown("Method & Project Description: Our stock prediction model is using a technical analysis approach at predicting the daily price movement of a stock and uses this data to attempt to predict future price movements.")
st.markdown("Demo:")


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")