import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np

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
strange_action_info = run_query("SELECT * from strange_action_info;")
video_info = run_query("SELECT * from video_info;")

# Print results.
st.subheader('돈방 내 재고 두수')
st.write(pd.DataFrame(
    pig_count,
    columns=['시점','돈방번호','재고두수']
))

st.subheader('돈방 이동정보')
st.write(pd.DataFrame(
    pig_movement,
    columns=['시점','복도번호','출처동방번호','목적지돈방번호','이동마릿수']
))

st.subheader('출하 돼지 마릿수')
st.write(pd.DataFrame(
    sold_pig,
    columns=['시점','출처돈방번호','츨히돼지수']
))

st.subheader('전체 영상정보')
st.write(pd.DataFrame(
    strange_action_info,
    columns=['날짜','영상파일경로']
))

st.subheader('이상행동 영상 정보')
st.write(pd.DataFrame(
    video_info,
    columns=['시점','돈방번호','데시벨']
))
