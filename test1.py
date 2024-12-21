import streamlit as st
st.write("Hello")
st.write("my first app EMC2")
st.title("EMC2 first app")
st.header("App for testing azure AI services")
st.subheader("test 1")
st.sidebar.image("https://seeklogo.com/images/E/ecole-hassania-des-travaux-publics-ehtp-logo-3D5770F217-seeklogo.com.png")
choix=st.sidebar.selectbox('Select app type', ['-- choose application --', 'Image analysis', 'Face analysis', 'OCR', 'Thumbnail Image'])
if choix== 'Image analysis':
  st.file_uploader('load image', type=['png', 'jpg', 'jpeg'])
