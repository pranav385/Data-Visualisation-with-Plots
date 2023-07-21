import streamlit as st
import pandas as pd
import numpy as np

# Instead of using streamlit library we can also use matplotlib
import matplotlib.pyplot as plt
import seaborn as sns # this is also a great library for data visualization. We can do many modification in seaborn for data visualization

chartData = pd  .DataFrame(np.random.randn(20,3), columns=['Line-1','Line-2',"Line-3"])

st.header('1. Charts with random numbers    ')

st.subheader("Our Randomly generated data")
st.write(chartData)

st.subheader('1.1 Line Chart')

st.line_chart(chartData)

st.subheader("1.2 Area Chart")

st.area_chart(chartData)

st.subheader("1.3 Bar Chart")

st.bar_chart(chartData)

st.header("2. Data Visualization with Matplotlib and Seaborn")

st.subheader('2.1 Loading the DataFrame')

df=pd.read_csv('iris.csv')

# st.dataframe(df)

# st.table(df) 

st.write(df) # from all three code data will be shown in webpage

st.subheader('2.2 Bar Graph with Matplotlib')

# Here we will use matplotlib

fig=plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

# Now we can see how to use seaborn

st.subheader('2.3 Distribution plot with Seaborn')
fig=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

# Now we can see how we can make multiple graph using steamlit

st.header("3. Multiple Graphs in one column")

# Now we need two column so we define two column

#KDE is for the line that comes with the graph

col1,col2=st.columns(2)

with col1:
    col1.header = 'KDE = False'
    col1.write('KDE=False')
    fig1 = plt.figure(figsize=(8,8))
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)


with col1:
    col1.header = 'KDE = False'
    col1.write('KDE=True') 
    fig1 = plt.figure(figsize=(8,8))
    sns.distplot(df['sepal_length'],kde=True)
    st.pyplot(fig1)

# hist is for the histoghram that comes in the graph

with col2:
    col2.header='hist=False'
    col2.write("Hist=False")
    fig2=plt.figure(figsize=(8,8))
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)


with col2:
    col2.header='hist=True'
    col2.write("Hist=True")
    fig2=plt.figure(figsize=(8,8))
    sns.distplot(df['sepal_length'],hist=True)
    st.pyplot(fig2)

    
# Now we will see how we can change the style of our plot

st.header("4. Changing Style")

col1,col2=st.columns(2)

with col1:
    col1.header = 'KDE = False'
    col1.write('KDE=False')
    fig1 = plt.figure()
    sns.set_style('darkgrid')  # to see more about the style se the documentation of seaborn
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],kde=False)
    st.pyplot(fig1)


with col1:
    col1.header = 'KDE = False'
    col1.write('KDE=True') 
    fig1 = plt.figure()
    sns.set_theme(context='poster',style='darkgrid')  # inside set_theme we can add multiple parameter
    sns.distplot(df['petal_length'],kde=True)
    st.pyplot(fig1)

# hist is for the histoghram that comes in the graph

with col2:
    col2.header='hist=False'
    col2.write("Hist=False")
    fig2=plt.figure(figsize=(8,8))
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)


with col2:
    col2.header='hist=True'
    col2.write("Hist=True")
    fig2=plt.figure(figsize=(8,8))
    sns.set_theme(context='notebook',style='darkgrid')
    sns.distplot(df['sepal_length'],hist=True)
    st.pyplot(fig2)


st.header('5. Exloring Diferent Graphs')

st.subheader('5.1 Scatter plot')

st.subheader("Here we are making plot by getting x and y axis")
fig,ax = plt.subplots(figsize=(15,8))

ax.scatter(np.random.randn(2,100),np.random.randn(2,100))
st.pyplot(fig)

st.subheader("Here we are making the plot using one axis by using * mark")
figN,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.randn(2,100))  # In scattered plot we need to give two axis x and y but if we give one axis then we can use * mark

st.pyplot(figN)

st.subheader("New One")
figu=plt.figure(figsize=(15,8))
plt.scatter(np.random.randn(2,100),np.random.randn(2,100))
st.pyplot(figu)

st.subheader("5.2 Count Plot")

fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x='species') # Here we are taking species column from df dataframe
st.pyplot(fig)


st.subheader("5.3 Box-Plot")

fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)


st.subheader('5.4 Violin-Plot')
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x='species',y='petal_length')
st.pyplot(fig)
