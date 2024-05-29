# stauthlib

Demo Repo

Please install ngrok.
In free version you have 1 static domain.

Register your auth app with Redirect URL: <https://ngrok-static-domain/login>

Add your auth app secrets under the separate auth section in `secrets.toml`

e.g.

```toml
[auth] #
redirect_uri = "https://rested-chicken-selected.ngrok-free.app/login"
[auth.google]
client_id = "...."
client_secret = "...."
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

[auth.microsoft]
client_id="...."
client_secret="..."
server_metadata_url="...."
```

- Run streamlit app: `streamlit run app.py`
- Run ngrok with static domain, e.g.: `ngrok http 8501 --domain rested-chicken-selected.ngrok-free.app`
