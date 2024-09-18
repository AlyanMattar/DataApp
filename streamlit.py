import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(layout='wide',initial_sidebar_state='expanded')
df = pd.read_csv('tips.csv')

# sidebar

st.sidebar.header('Tips Dashboard')
st.sidebar.image('4_tips._nutcd32.jpg')
st.sidebar.write('This is Dashboard have been created from tips dataset for educational purposes.')
st.sidebar.write('')
st.sidebar.markdown('Created by [Eleyan](https://gist.github.com/rxaviers/7360908) :hushed:')
st.sidebar.write('')
cat_filter = st.sidebar.selectbox('Categorical Filtering',[None,'sex','smoker','day','time'])
num_filter = st.sidebar.radio('Numerical Filtering',[None,'tip','total_bill'])
row_filter = st.sidebar.radio('Row Filtering',[None,'sex','smoker','day','time'])
col_filter = st.sidebar.radio('column Filtering',[None,'sex','smoker','day','time'])


# body

a1, a2, a3, a4 = st.columns(4)

a1.metric('Max. Total Bills',df['total_bill'].max())
a2.metric('Min. Total Bills',df['total_bill'].min())
a3.metric('Max. Tips',df['tip'].max())
a4.metric('Min. Tips',df['tip'].min())
st.subheader('Total bill vs. tip')
fig = px.scatter(data_frame = df,x = 'total_bill',y='tip',color=cat_filter,size=num_filter,facet_col=col_filter,facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True)
c1, c2, c3 = st.columns((3,4,4))
with c1:
    st.write('Tips vs. smoker-nonsmoker')
    fig = px.pie(data_frame=df,names='smoker',values='tip')
    st.plotly_chart(fig,use_container_width=True)
with c2:
    st.write('Tips vs. sex')
    fig = px.bar(data_frame=df,x='sex',y='tip',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
with c3:
    st.write('Tips vs. days')
    fig = px.pie(data_frame=df,names='day',values='tip',hole=0.4)
    st.plotly_chart(fig,use_container_width=True)








