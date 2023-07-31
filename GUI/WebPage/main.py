import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")

content1 = """
Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consequatur minima modi at nulla sit aliquid perferendis excepturi, amet molestias et repellat tenetur, facere fugiat vero placeat accusamus esse optio magni.
Eum enim quaerat aliquam nobis itaque. Sunt rem nam iste tenetur illo, est quis aspernatur soluta velit beatae molestiae tempora ratione odit adipisci et maiores at laudantium. Fuga, dolorum quidem?
Fugit eligendi voluptatum, nemo amet dolore alias architecto maiores soluta ipsa atque a doloribus asperiores at distinctio praesentium minima nisi reprehenderit iure quam neque libero dolorum commodi. Voluptatem, doloremque. Animi!"""
st.write(content1)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
