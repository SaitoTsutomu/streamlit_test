import pandas as pd
import streamlit as st

st.header("数学の試験の成績の検索")
df = pd.read_csv("exam.csv", encoding="utf-8")
s = st.text_input("クエリ")
if s:
    try:
        result = df.query(s)
        st.dataframe(result)
    except:
        st.error("クエリを正しくしてください")
