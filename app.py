import streamlit as st

st.title('CampusX')

col1,col2=st.columns(2)

with col1:
    st.image('Night_sky.jpg')

with col2:
    st.header('CampusX is an Online platform')

st.header('Courses')
st.subheader('DSMP')
st.subheader('DSAP')
st.subheader('DSEP')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- home
- about
- contact
- career
- login""")

st.sidebar.selectbox('Select one',['teacher','student'])
st.sidebar.button('Select')