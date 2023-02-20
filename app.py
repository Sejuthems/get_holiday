

import jpholiday
import datetime
import streamlit as st




# Making columns

col1, col2 = st.columns(2)
with col1:
   st.header("START")
   d1 = st.date_input("Select START", datetime.date(2019, 7, 6))
   st.write(d1)

with col2:
   st.header("END")
   d2 = st.date_input("Select END", datetime.date(2019, 7, 6))

   
if st.button("実行"):
   kitni_cutti = jpholiday.between(d1, d2)
   for dayitem in kitni_cutti:
      i = 1
      st.write(str(i) + ". " + dayitem[0].strftime("%Y/%m/%d") + "   " + dayitem[1])
      i = i +1
      


"""
# datetime.date
kitni_cutti = jpholiday.between(datetime.date(2017, 1, 2), datetime.date(2017, 5, 3))
kitni_cutti
kitni_cutti[1][0]
kitni_cutti[1][0].strftime("%d")

for dayitem in kitni_cutti:
    i = 1
    st.write(str(i) + ". " + dayitem[0].strftime("%Y/%m/%d") + "   " + dayitem[1])
    i = i + 1


######################################################

import datetime
import streamlit as st

#Input for date


import streamlit as st

#Chnage here to column 2
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

######################################################################


from datetime import datetime as lol

now = lol.now() # current date and time
type(now)
year = now.strftime("%Y/%m/%d")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)
"""
