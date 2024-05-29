import streamlit as st

st.title("Hello World!")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

google_button = st.button("Login WITH Google")

if google_button:
    st.experimental_user.login(send_redirect_to_host=False, provider="google")


auth_login = st.button("Authlib Login")
if auth_login:
    st.experimental_user.login(send_redirect_to_host=False, provider="auth0")


microsoft_login = st.button("Microsoft Login")

if microsoft_login:
    st.experimental_user.login(send_redirect_to_host=False, provider="microsoft")

st.write(st.experimental_user)


logout_button = st.button("Logout")

if logout_button:
    st.experimental_user.logout()
