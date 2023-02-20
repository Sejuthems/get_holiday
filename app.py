

import jpholiday
import datetime
import streamlit as st


st.set_page_config(page_title="Debt Collection project")
st.header("債権回収自動コールシステム_PHASE-3")
st.subheader("下記のところにエクセルのファイルアップしてください")



# Making columns

col1, col2 = st.columns(2)
with col1:
   st.header("START")
   d1 = st.date_input("Select START", datetime.date(2019, 7, 6))

with col2:
   st.header("END")
   d2 = st.date_input("Select END", datetime.date(2019, 7, 6))

   
if st.button("実行"):
   kitni_cutti = jpholiday.between(d1, d2)
   i = 1
   for dayitem in kitni_cutti:
      st.write(str(i) + ". " + dayitem[0].strftime("%Y/%m/%d") + "   " + dayitem[1])
      i = i +1
      
