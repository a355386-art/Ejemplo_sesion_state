import streamlit as at
st.title ("Ejemplo para usarpara usar session_state")

count = 0

increment = st.button("increment")
if increment: 
  count += 1
  
st.write("count =", count)
