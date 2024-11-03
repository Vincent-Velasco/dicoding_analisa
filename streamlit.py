import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

bike_df = pd.read_csv("./day.csv")

st.title("Welcome to my Dicoding Analisa Dashboard Website")
st.header("My name is Vincent Velasco")

col1, col2 = st.columns(2)

with col1:
    st.write("Pertanyaan 1: Apakah ada hubungan antara hari libur atau hari kerja dengan jumlah rental sepeda?")

    bike_df_day = bike_df[["workingday", "casual", "registered", "cnt"]]
    
    bike_df_day_group = bike_df_day.groupby("workingday").mean()

    st.write("Table group by working day")
    st.table(bike_df_day_group)

    st.write("Conclusion pertanyaan 1:Kurang lebih tidak ada hubungan antara jumlah rental sepeda dengan hari kerja atau tidak, tetapi bisa dilihat bahwa di hari kerja, jumlah user yang registered signifikan lebih banyak dibandingkan casual user, sehingga bisa dikatakan bahwa banyak user yang menggunakan rental sepeda untuk berangkat kerja")


with col2:
    st.write("Pertanyaan 2: Apakah ada peningkatan dari rental sepeda selama 2 tahun berjalan?")

    bike_df_month = bike_df[["dteday", "casual", "registered", "cnt"]]
    
    bike_df_month["dteday"] = pd.to_datetime(bike_df_month["dteday"])
    
    bike_df_month = bike_df_month.groupby(pd.Grouper(key = "dteday", freq = 'M')).sum()
    
    # fig = plt.figure(figsize = (15,10))
    # plt.plot(bike_df_month)
    # plt.legend(["Casual", "Registered", "Total"])
    # plt.show()
    st.write("Line Chart by Month")
    st.line_chart(bike_df_month)

    st.write("Conclusion pertanyaan 2: Di setiap tahunnya mengalami peningkatan jumlah rental sepeda (sehingga bisa untuk menambahkan lokasi atau ekspansi rental sepeda), tetapi pada awal dan akhir tahun akan mengalami penuruan dalam jumlah rental sepeda dan juga peak dari rental sepeda berada di tengah tahun")
