import glob
import streamlit as st
from backend import directory, extension

st.title("Diary Entries")

files = sorted(glob.glob(f"{directory}*{extension}"))

for file in files:
    date = file[len(directory):-len(extension)]
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    st.subheader(date)
    st.write(text)
