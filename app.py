import streamlit as st

st.title("Auth demo!")


with st.echo():
    st.write("Is user logged in?", st.experimental_user.is_logged_in())

left, middle, right, logout_button_column = st.columns(4)


with left:
    google_button = st.button("Login with Google")

    if google_button:
        st.experimental_user.login(provider="google")

with middle:
    auth_zero_login = st.button("Auth0 Login")
    if auth_zero_login:
        st.experimental_user.login(provider="auth0")

with right:
    microsoft_login = st.button("Microsoft Login")

    if microsoft_login:
        st.experimental_user.login(provider="microsoft")


st.write(":sparkles: :rainbow[User data]")
st.write(st.experimental_user)


with logout_button_column:
    logout_button = st.button("Logout")
    if logout_button:
        st.experimental_user.logout()
