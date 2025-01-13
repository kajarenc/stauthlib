import streamlit as st

st.title("Auth demo!")


left, middle1, middle2, right, logout_button_column = st.columns([1, 1, 1, 1.1, 1])


with left:
    google_button = st.button("Google Login")

    if google_button:
        st.login(provider="google")

with middle1:
    auth_zero_login = st.button("Auth0 Login")
    if auth_zero_login:
        st.login(provider="auth0")

with middle2:
    okta_login = st.button("Okta Login")
    if okta_login:
        st.login(provider="okta")

with right:
    microsoft_login = st.button("Microsoft Login")

    if microsoft_login:
        st.login(provider="microsoft")


st.write(":sparkles: :rainbow[User data]")
st.write(st.experimental_user)


with logout_button_column:
    logout_button = st.button("Logout")
    if logout_button:
        st.logout()


st.header("Streamlit app code:")
st.code(
    body="""
    google_button = st.button("Google Login")

    if google_button:
        st.login(provider="google")
    """,
    language="python",
)

st.header("Secrets.toml file example:")
with open("./.streamlit/secrets.toml.example", "r") as f:
    st.code(f.read(), language="toml")
