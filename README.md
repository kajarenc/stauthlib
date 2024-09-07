# stauthlib

This is a prototype for authentication in Streamlit. It supports all OAuth 2 providers (e.g., Google, Microsoft, GitHub, etc.). 

## Usage

1. Sign up for [ngrok](https://ngrok.com/) and install it on your machine. Make sure to create a static URL at the end of their sign-up flow. ngrok is required to test authentication locally. The OAuth provider (e.g., Google) redirects to a URL after the user successfully signs in and sends all sign-in information there. That URL needs to be publicly available on the internet. But if you test your app locally, your app will only have a localhost URL. ngrok solves this by tunneling your localhost URL to a public URL on the internet. Note that you don't need ngrok when deploying since the URL is already public in that case. 
2. Clone this repo: `git clone https://github.com/kajarenc/stauthlib`
3. Install the requirements: `pip install -r requirements.txt`. Note that this will install a custom Streamlit wheel from [this PR](https://github.com/streamlit/streamlit/pull/8786/files).
4. Run the Streamlit app: `streamlit run streamlit_app.py`
5. Run ngrok: `ngrok http 8501 --domain <your-static-ngrok-url>`. Insert the static ngrok URL you created while signing up for ngrok. You can now go to this URL in your browser and check that you can access your local app through it. 
6. Create a client ID and client secret from your OAuth provider. E.g. for Google, there's a good explanation [here](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid). Note that you have to provide the redirect URI to the provider, which is `<your-static-ngrok-url>/oauth2callback`. 
7. Add the redirect URI (`<your-static-ngrok-url>/oauth2callback`), client ID, and client secret to `.streamlit/secrets.toml`. You can remove the code for providers you don't use. 
8. Go to your app on the public ngrok URL and click on your provider's login button. You should now be able to log in and then be redirected back to your app!

## API

With the wheel file in this repo, you can use the following commands in your Python code:

- `st.experimental_user` shows you information about the user when logged in (e.g., their email, name, and avatar image). This information comes from the OAuth provider.
- `st.experimental_user.login(provider="google")` will send the user to the OAuth provider and let them log in. After login, they will be redirected to the app. Note that a user can only be signed in with one provider at a time, i.e. logging in with a different provider will log them out of the previous one. 
- `st.experimental_user.logout()` will log out a signed-in user. 

See [app.py](https://github.com/kajarenc/stauthlib/blob/main/app.py) for a full example of how to use this code. 



