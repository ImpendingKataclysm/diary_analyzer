import streamlit as st
import plotly.express as px
from backend import pos_scores, neg_scores, dates

st.title("Diary Sentiment Analysis")
st.subheader("Positivity")

figure = px.line(x=dates, y=pos_scores, labels={"x": "Date",
                                                "y": "Positivity Score"})
st.plotly_chart(figure)
