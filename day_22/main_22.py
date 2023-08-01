import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
Python is a popular high-level programming language known for its simplicity and readability.
It is widely used for web development, data analysis, artificial intelligence, and more. 
Python's extensive library ecosystem and vibrant community make it a versatile choice for both beginners 
and experienced developers. With its clean syntax and emphasis on code readability, 
Python is a great language for anyone looking to start their journey into programming.
"""
st.info(content)

st.title("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv(r"c:\projects\Camp-60-Days-of-Code\day_22\data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        full_name = row["first_name"].capitalize() + " " + row["last_name"].capitalize()
        st.title(full_name)
        st.write(row["role"])
        with open(rf"c:\projects\Camp-60-Days-of-Code\day_22\images\{row['image']}", "rb") as f:
            image = f.read()
        st.image(image)

with col2:
    for index, row in df[4:8].iterrows():
        full_name = row["first_name"].capitalize() + " " + row["last_name"].capitalize()
        st.title(full_name)
        st.write(row["role"])
        with open(rf"c:\projects\Camp-60-Days-of-Code\day_22\images\{row['image']}", "rb") as f:
            image = f.read()
        st.image(image)

with col3:
    for index, row in df[8:].iterrows():
        full_name = row["first_name"].capitalize() + " " + row["last_name"].capitalize()
        st.title(full_name)
        st.write(row["role"])
        with open(rf"c:\projects\Camp-60-Days-of-Code\day_22\images\{row['image']}", "rb") as f:
            image = f.read()
        st.image(image)
