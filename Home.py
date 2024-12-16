import streamlit as st
import pandas  # To read the csv file

data_frame = pandas.read_csv("data/data.csv", sep=';')

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

content_my_apps = """Below you can find some apps I have built. Feel free to contact me."""
st.write(content_my_apps)

colL2, col2_empty, colR2 = st.columns([1.5, 0.5, 1.5])

with colL2:
    for i, row in data_frame[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with colR2:
    for i, row in data_frame[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")