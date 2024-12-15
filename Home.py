import streamlit as st

st.set_page_config(layout="wide")

colL, colR = st.columns(2)

with colL:
    st.image("images/photo.png")

with colR:
    st.title("Sum Yung Guy")
    contentR = """Fusce neque mauris, porta elementum mi at, hendrerit tempus lectus. Donec finibus, 
    tellus eu venenatis malesuada, enim sem dapibus lectus, in convallis purus magna et velit. 
    Aliquam semper libero vel ipsum feugiat, eget ullamcorper eros pretium. """
    st.info(contentR)