import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    with open(r"c:\projects\Camp-60-Days-of-Code\day_21\images\photo.png", "rb") as f:
        image = f.read()
    st.image(image)

with col2:
    st.title("Dima")
    content = """
    Python is a popular high-level programming language known for its simplicity and readability.
    It is widely used for web development, data analysis, artificial intelligence, and more. 
    Python's extensive library ecosystem and vibrant community make it a versatile choice for both beginners 
    and experienced developers. With its clean syntax and emphasis on code readability, 
    Python is a great language for anyone looking to start their journey into programming.
    """
    st.info(content)

content2 = """
Bellow you can find some of apps I have built in Python.
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv(r"c:\projects\Camp-60-Days-of-Code\day_21\data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        with open(rf"c:\projects\Camp-60-Days-of-Code\day_21\images\{row['image']}", "rb") as f:
            image = f.read()
        st.image(image)
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        with open(rf"c:\projects\Camp-60-Days-of-Code\day_21\images\{row['image']}", "rb") as f:
            image = f.read()
        st.image(image)
        st.write(f"[Source Code]({row['url']})")