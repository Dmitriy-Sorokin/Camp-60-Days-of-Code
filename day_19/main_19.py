import streamlit as st
import functions


def write(a):
    # with open(r"c:\local git reposiroty\Camp-60-Days-of-Code\day_19\hello.txt", "a") as file:
    with open(r"c:\projects\Camp-60-Days-of-Code\day_19\hello.txt", "a") as file:
        a = file.writelines(f"{a}\n")
        return a


def read():
    # with open(r"c:\local git reposiroty\Camp-60-Days-of-Code\day_19\hello.txt", "r") as file:
    with open(r"c:\projects\Camp-60-Days-of-Code\day_19\hello.txt", "r") as file:
        b = file.readlines()
        return b


def write_w(a):
    # with open(r"c:\local git reposiroty\Camp-60-Days-of-Code\day_19\hello.txt", "r") as file:
    with open(r"c:\projects\Camp-60-Days-of-Code\day_19\hello.txt", "w") as file:
        a = file.writelines(f"{a}\n")
        return a


def add():
    todo = st.session_state["new_todo"]
    return write(todo)


st.title("My todo App")
st.subheader("This my")
st.write("simple text")

list_words = read()
for index, item in enumerate(list_words):
    checkbox = st.checkbox(item, key=index)
    if checkbox:
        list_words.pop(index)
        for i in list_words:
            write_w(i)
        del st.session_state[list_words]
        st.experimental_rerun()

st.text_input(label="Enter", placeholder="add new tod", on_change=add, key="new_todo")

st.session_state
