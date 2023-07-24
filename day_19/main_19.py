import streamlit as st
import functions


def write(a):
    with open(r"c:\local git reposiroty\Camp-60-Days-of-Code\day_19\hello.txt", "a") as file:
        a = file.writelines(f"\n{a}")
        return a

def read():
    with open(r"c:\local git reposiroty\Camp-60-Days-of-Code\day_19\hello.txt", "r") as file:
        b = file.readlines()
        return b



def add():
    todo = st.session_state["new_todo"]
    b = write(todo)
    return b


st.title("My todo App")
st.subheader("This my")
st.write("simple text")


f = read()
for item in f:
    st.checkbox(item)

st.text_input(label="Enter", placeholder="add new tod", on_change=add, key="new_todo")

st.session_state
