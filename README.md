# stauthlib

This is a prototype for authentication in Streamlit. It supports all OIDC providers (e.g., Google, Microsoft etc.).

## Usage

1. Clone this repo: `git clone https://github.com/kajarenc/stauthlib`
2. Install the requirements: `pip install -r requirements.txt`. Note that this will install a custom Streamlit wheel from [this PR](https://github.com/streamlit/streamlit/pull/8786/files).
3. Run the Streamlit app: `streamlit run app.py`
4. Create a client ID and client secret from your OAuth provider. E.g. for Google, there's a good explanation [here](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid). Note that you have to provide the redirect URI to the provider, which is `http://localhost:8501/oauth2callback`.
5. Add the redirect URI (`http://localhost:8501/oauth2callback`), client ID, and client secret to `.streamlit/secrets.toml`. You can remove the code for providers you don't use.
6. Go to your app on `http://localhost:8501` and click on your provider's login button. You should now be able to log in and then be redirected back to your app!

## API

With the wheel file in this repo, you can use the following commands in your Python code:

- `st.experimental_user` shows you information about the user when logged in (e.g., their email, name, and avatar image). This information comes from the OAuth provider.
- `st.experimental_user.login(provider="google")` will send the user to the OAuth provider and let them log in. After login, they will be redirected to the app. Note that a user can only be signed in with one provider at a time, i.e. logging in with a different provider will log them out of the previous one.
- `st.experimental_user.logout()` will log out a signed-in user.

See [app.py](https://github.com/kajarenc/stauthlib/blob/main/app.py) for a full example of how to use this code.
