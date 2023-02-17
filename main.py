import streamlit as st
import plotly.express as px
from backend import pos_scores, neg_scores, dates

st.title("Diary Sentiment Analysis")
st.subheader("Positivity")

pos_graph = px.line(x=dates, y=pos_scores, labels={"x": "Date",
                                                   "y": "Positivity Score"})
st.plotly_chart(pos_graph)

st.subheader("Negativity")

neg_graph = px.line(x=dates, y=neg_scores, labels={"x": "Date",
                                                   "y": "Negativity Score"})
st.plotly_chart(neg_graph)
