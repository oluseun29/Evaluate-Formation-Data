print("hello")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header('Data Header')
    st.write(dataframe.head())



def data_plot(dataframe):
    
    fig, ax = plt.subplots(1,1)
    ax.hist(x = dataframe['GR'])
    ax.set_xlabel('GR')
    st.pyplot(fig)

    
    fig, ax = plt.subplots(1,1)
    ax.hist(x = dataframe['NPHI'])
    ax.set_xlabel('NPHI')
    st.pyplot(fig)
    
    fig, ax = plt.subplots(1,1)
    ax.hist(x = dataframe['RHOB'])
    ax.set_xlabel('RHOB')
    st.pyplot(fig) 

    fig, ax = plt.subplots(1,1)
    ax.hist(x = dataframe['DTC'])
    ax.set_xlabel('DTC')
    st.pyplot(fig)  



st.title("Evaluate Formation Data")
st.text("This is a web app to Evaluate Formation Data")

st.sidebar.title('Navigation')


uploaded_file = st.sidebar.file_uploader("Upload your file here")

options = st.sidebar.radio('Pages', options= ['Home','Data Statistics', 'Data Header', 'Histograms'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
   
    
if options == "Data Statistics":
    stats(df)

elif options == "Data Header":
    data_header(df)

elif options == 'Histograms':
    data_plot(df)


    
