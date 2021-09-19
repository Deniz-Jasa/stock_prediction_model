import streamlit as st
import time
import numpy as np
import pandas as pd
import rsi_converted as dt

# Web app title:
st.write("""
# Simple Stock Predictor App
""")

# Description:
st.markdown("Our Group: Khuong Tran, Deniz Jasarbasic, Eric Karpovits, Raz Levi")
st.markdown("Language: Python")
st.markdown("Technologies:")
st.markdown("Method & Project Description: Our stock prediction model is using a technical analysis approach at predicting the daily price movement of a stock and uses this data to attempt to predict future price movements.")
st.markdown("Demo:")





st.markdown("Confusion Matrix Visualization:")

# Visualization of the Confusion Matrix:
df = pd.DataFrame(
    dt.prediction,
    columns=('col %d' % i for i in range(500)))

#st.dataframe(df)
#st.plotly_chart(df)
streamlit.pyplot(fig=None, clear_figure=None, **df)

# Reruns the web app:
st.button("Re-run")