import streamlit as st
import mysql.connector
import pandas as pd

st.title('양돈관리')

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

pig_count = run_query("SELECT * from pig_count;")
pig_movement = run_query("SELECT * from pig_movement;")
sold_pig = run_query("SELECT * from sold_pig;")
strange_action_info = run_query("SELECT * fromstrange_action_info;")
video_info = run_query("SELECT * from video_info;")

# Print results.
st.write(pd.DataFrame({
    pig_count
}))