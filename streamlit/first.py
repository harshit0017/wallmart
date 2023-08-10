import streamlit as st 
import pandas as pd
st.write("hello streamlit")
st.markdown(":green[$\sqrt{x+y}=1$] is a pythogorean identity. :pencil:")
st.title("Upload a file and watch it ")
data= st.file_uploader("upload")
st.dataframe(data)
