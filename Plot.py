import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

import plotly.express as px
import plotly.figure_factory as ff

# Altair Scattered Plot
st.header('1. Altair Scatter Plot')

chartData = pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart = alt.Chart(chartData).mark_circle().encode(x='a',y='b',size='c',
                tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

data=pd.DataFrame(np.random.randn(10,3),columns=['a','b','c'])
chartData1 = data

st.write(data)

chart1 = alt.Chart(chartData1).mark_circle().encode(x='a',y='b',size='c',
                tooltip=['a','b','c'])
st.altair_chart(chart1)

st.header("2. Interactive Charts")

st.subheader('2.1 Line Chart')

df =pd.read_csv('lang_data.csv')
lang_list = df.columns.tolist() # this will convert the column into list

st.write(lang_list)

# Now we make a multiple select option so that we can select multiple column and compare so we use multiselect
lang_choices = st.multiselect('Choose your language', lang_list)
new_df = df[lang_choices] # What ever options we are selecting we are creating dataframe for that only
st.write(new_df)
st.line_chart(new_df)

st.subheader('2.2 Area Chart')

df1 = pd.read_csv('lang_data.csv')
lang_list1 = df1.columns.tolist()

lang_choices1=st.multiselect('Choose your Preferred language',lang_list1)
new_df1=df[lang_choices1]
st.area_chart(new_df1)

# Plotly most important library for data visualization


st.header("3. Data Visualization with Plotly")

st.subheader('3.1 Displaying the DataSet')

df = pd.read_csv('tips.csv')
st.dataframe(df.head())

st.subheader('3.2 Pie Charts')

fig=px.pie(df, values = 'total_bill', names='day') # in values we write which column we want to take to make the dataframe
# in name we will take what to name the pie chart.
st.plotly_chart(fig)

st.subheader('New Pie Charts')

fig=px.pie(df, values = 'total_bill', names='time') # in values we write which column we want to take to make the dataframe
# in name we will take what to name the pie chart.
st.plotly_chart(fig)

st.subheader('New Pie Charts')

fig=px.pie(df, values = 'total_bill', names='size') # in values we write which column we want to take to make the dataframe
# in name we will take what to name the pie chart.
st.plotly_chart(fig)


st.subheader('3.3 Pie Charts with multiple parameter')

fig=px.pie(df, values = 'total_bill', names='size',opacity=.7, 
           color_discrete_sequence = px.colors.sequential.RdBu) 
# in values we write which column we want to take to make the dataframe
# in name we will take what to name the pie chart.
st.plotly_chart(fig)


st.header('4. Histogram')

st.subheader("4.1 ")

x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_labels=["Group - 1","Group - 2","Group - 3"]
fig=ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])

st.plotly_chart(fig)

x11 = np.random.randn(10)
# x21 = np.random.randn(200)
# x31 = np.random.randn(200)

st.write(x11)

hist_data = [x11]
group_labels=["Group - 1"]
fig1=ff.create_distplot(hist_data,group_labels,bin_size=[.1])

st.plotly_chart(fig1)