import streamlit as st

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
Hello world
"""

st.write(content2)
