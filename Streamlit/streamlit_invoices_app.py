import streamlit as st 
import pandas as pd
#import numpy as np  
import seaborn as sns
import matplotlib.pyplot as plt
#import plotly.express as px



tips_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

pages = ["Goal's project", "Global view of dataset", "Data visualisation", "Conclusion"]

page = st.sidebar.radio("Go to page :", pages)

if page == pages[0] : 
    
    st.write("### Goal's project")
    
    st.write("The goal of this challenge is to analyze a restaurant invoices from file *tips.csv file*. In order to meet this challenge, we are going to answer some questions :")
    
    st.write(" * What is the best day for the restaurant owner ?")
    st.write(" * What is the best day for waiters ?")
    st.write(" * What is the profile of people who are going to the restaurant and what is the best time to go ?")
    
    st.image("resto_141793-2866.jpg")
    
elif page == pages[1]:
    st.write("### Global view of dataset")
    
    st.dataframe(tips_df.head())
    
    st.write("Dataframe dimension :")
    
    st.write("Dataset contains respectively "+ str(tips_df.shape) + " rows and columns")
 
    st.write("The restaurant is open " + str(len(tips_df['day'].unique())) + " days per week")
    
    st.write(tips_df.nlargest(1,columns='total_bill'))
    
    st.write("The day of the week when there is more bill is : Saturday")
    
    if st.checkbox("Show missing values") :
        st.dataframe(tips_df.isna().sum())
        
    if st.checkbox("Show duplicated values") :
        st.write(tips_df.duplicated().sum())
        
    duplicates = tips_df[tips_df.duplicated()]

    st.write("Remove duplicates : " + str(tips_df.drop_duplicates(keep = 'first', inplace=True)))
    
    if st.checkbox("Check the duplicated values") :
        st.write(tips_df.duplicated().sum())
    
elif page == pages[2]:
    st.write("### Data visualisation")
    
    #st.subheader ("###### Plotting with Seaborn")
    
    st.write(" * Plotting with Seaborn by day") 
    
    fig_sb, ax_sb = plt.subplots()
    ax_sb = sns.countplot(data=tips_df, x='day', order=['Thur', 'Fri', 'Sat', 'Sun'])
    plt.xlabel("Days")
    st.pyplot(fig_sb)

    st.write(" Observation : the day when there is more activity is Saturday, like we observe in the previous page 'Global view of dataset'")

    st.write(" * Plotting by Tips") 
    fig_mt = sns.catplot(data=tips_df, x='day', y='tip', kind="bar", order=['Thur', 'Fri', 'Sat', 'Sun'])
    plt.xlabel("Count of tips per day")
    st.pyplot(fig_mt)
    
    st.write(" Observation : there are more tips on Sunday")

    st.write(" * Plotting by Category of people") 
    fig2_sb, ax3_sb = plt.subplots()
    ax3_sb = sns.countplot(data=tips_df, x="sex")
    plt.xlabel("Sex")
    st.pyplot(fig2_sb)
    
    st.write(" Observation : more men go to restaurant than women")
    
    st.write(" * Plotting by smoker") 
    fig3_sb, ax3_sb = plt.subplots()
    sns.countplot(data=tips_df, x='smoker')
    plt.xlabel("smoker")
    st.pyplot(fig3_sb)
    
    st.write(" Observation : non smoker go to restaurant more than smoker")    
    
    st.write(" * Plotting by Time") 
    fig4_sb, ax4_sb = plt.subplots()
    ax4_sb = sns.countplot(data=tips_df, x="time")
    plt.xlabel("Time")
    st.pyplot(fig4_sb)

    st.write(" Observation : Dinner is the best time to go to restaurant")     


elif page == pages[3]:
    st.write("### Conclusion")
    
    st.write("After this data exploratory analysis, we can conclude that :") 
    st.write(" * Saturday is the best day for restaurant's owner and Sunday is a good day for waiters who get more tips")
    st.write(" * Men go to restaurants more often than women and there are more of non smokers")
    st.write(" * People prefer going to the restaurant for the dinner")
  
  
  
  
  
  # In the terminal, wtype : "streamlit run streamlit_invoices_app.py"