

import jpholiday
import datetime
import streamlit as st


st.set_page_config(page_title="Holidays Japan")
st.header("休日計算")
st.subheader("休日期間をお選びください")



# Making columns

col1, col2 = st.columns(2)
with col1:
   st.header("始")
   d1 = st.date_input("Select START", datetime.date(2019, 7, 6))

with col2:
   st.header("終")
   d2 = st.date_input("Select END", datetime.date(2019, 7, 6))

   
if st.button("実行"):
   kitni_cutti = jpholiday.between(d1, d2)
   i = 1
   for dayitem in kitni_cutti:
      st.write(str(i) + ". " + dayitem[0].strftime("%Y/%m/%d") + "   " + dayitem[1])
      i = i +1
      
