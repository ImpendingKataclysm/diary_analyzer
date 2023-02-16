import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))
analyzer = SentimentIntensityAnalyzer()
negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    print(scores)
