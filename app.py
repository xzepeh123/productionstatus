import streamlit as st
import pandas as pd

st.set_page_config(page_title="Production Status", layout="wide")

df = pd.read_excel(r"C:\Users\PLC Engineer\Desktop\test.xlsx")

# ---------------------- KPI Summary ----------------------
st.markdown(
    """
    <div style='background:#F0F2F6;padding:10px 12px;border-radius:8px;text-align:center;'>
        <h4 style='margin-bottom:10px;'>👥 Total Customers</h4>
        <h2 style='color:#1f77b4;'>{:,}</h2>
    </div>
    """.format(df['id'].nunique()),
    unsafe_allow_html=True
)
