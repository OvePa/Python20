import requests
import streamlit as st
import os

API_NASA = os.getenv("NASA_API")
url = f"https://api.nasa.gov/planetary/apod?api_key={API_NASA}"

# Get request data as dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image = "img.png"
response2 = requests.get(image_url)
with open(image, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image)
st.write(explanation)
