import requests
import streamlit as st

st.title("Auth demo!")

left, middle, right, far_right = st.columns(4)


with left:
    google_button = st.button("Login with Google")

    if google_button:
        st.experimental_user.login(provider="google")

with middle:
    auth_login = st.button("Authlib Login")
    if auth_login:
        st.experimental_user.login(provider="auth0")

with right:
    microsoft_login = st.button("Microsoft Login")

    if microsoft_login:
        st.experimental_user.login(provider="microsoft")


st.write(":sparkles: :rainbow[User data]")
st.write(st.experimental_user)


with far_right:
    logout_button = st.button("Logout")
    if logout_button:
        st.experimental_user.logout()
