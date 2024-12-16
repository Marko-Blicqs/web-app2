import streamlit as st
import pandas

def write_contacts(column, co_data, start, end):
    with column:
        for i, row in co_data[start:end].iterrows():
            st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
            st.write(row['role'])
            st.image("company_data/images/" + row["image"], width=130)


company_data = pandas.read_csv("company_data/data.csv")
page_description = """
Fusce neque mauris, porta elementum mi at, hendrerit tempus lectus. Donec finibus, 
    tellus eu venenatis malesuada, enim sem dapibus lectus, in convallis purus magna et velit. 
    Aliquam semper libero vel ipsum feugiat, eget ullamcorper eros pretium.
"""

st.set_page_config(layout="wide")
st.header("The Best Company")
st.write(page_description)
st.subheader("Our Team")

colL, colM, colR = st.columns(3)
write_contacts(colL, company_data, 0, 4)
write_contacts(colM, company_data, 4, 8)
write_contacts(colR, company_data, 8, 112)