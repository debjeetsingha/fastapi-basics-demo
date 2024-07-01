import streamlit as st
import requests

# FastAPI endpoint URL
api_url = "http://127.0.0.1:8000/api/randomname"

st.title("Random Name Generator")

if st.button('Fetch Random Name'):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if 'name' in data:
            st.success(f"Random Name: {data['name']}")
        else:
            st.error("The response does not contain a 'name' field.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching the data: {e}")
