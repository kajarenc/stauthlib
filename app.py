import requests
import streamlit as st

st.title("Auth demo!")


@st.cache_data
def get_github_user_identity(access_token):
    if not access_token:
        return None

    headers = {"Authorization": "token " + access_token}
    response = requests.get(
        "https://api.github.com/user",
        headers=headers,
    )

    data = response.json()

    if not data.get("email"):
        response = requests.get(
            "https://api.github.com/user/emails",
            headers=headers,
        )
        data["email"] = next(
            email["email"] for email in response.json() if email["primary"]
        )
    return data


google_button = st.button("Login with Google")

if google_button:
    st.experimental_user.login(provider="google")


auth_login = st.button("Authlib Login")
if auth_login:
    st.experimental_user.login(provider="auth0")


microsoft_login = st.button("Microsoft Login")

if microsoft_login:
    st.experimental_user.login(provider="microsoft")

github_login = st.button("Github Login")

if github_login:
    st.experimental_user.login(provider="github")


st.write(":sparkles: :rainbow[User data]")
st.write(st.experimental_user)

if st.experimental_user.get("provider") == "github":
    github_access_token = st.experimental_user.get("access_token")
    st.write(":sparkles: :rainbow[Github user data]")
    st.write(get_github_user_identity(github_access_token))


logout_button = st.button("Logout")

if logout_button:
    st.experimental_user.logout()
