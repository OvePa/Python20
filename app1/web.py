import streamlit as st
import functions

todos = functions.get_todos()

st.title('My Todo App')
st.subheader("subheader")
st.write("texto")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a Todo:',placeholder='Add new todo...')