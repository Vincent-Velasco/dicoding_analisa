import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

bike_df = pd.read_csv("/day.csv")

st.title("Welcome to my Dicoding Analisa Dashboard Website")
st.header("My name is Vincent Velasco")

col1, col2 = st.columns(2)

with col1:
    #- Pertanyaan 1: Apakah ada hubungan antara hari libur atau hari kerja dengan jumlah rental sepeda?

    bike_df_day = bike_df[["workingday", "casual", "registered", "cnt"]]
    
    bike_df_day_group = bike_df_day.groupby("workingday").mean()
    
    print(bike_df_day_group)


with col2:
    #Pertanyaan 2: Apakah ada peningkatan dari rental sepeda selama 2 tahun berjalan?

    bike_df_month = bike_df[["dteday", "casual", "registered", "cnt"]]
    
    bike_df_month["dteday"] = pd.to_datetime(bike_df_month["dteday"])
    
    bike_df_month = bike_df_month.groupby(pd.Grouper(key = "dteday", freq = 'M')).sum()
    
    fig = plt.figure(figsize = (15,10))
    plt.plot(bike_df_month)
    plt.legend(["Casual", "Registered", "Total"])
    plt.show()
