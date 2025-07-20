from fastapi import FastAPI
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import httpx, os, google.auth.transport.requests

load_dotenv()
app = FastAPI()
SCOPES = os.getenv("SCOPES")
CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")
VIEWS = os.getenv("VIEWS")
VIDEO = os.getenv("VIDEO")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stats")
async def read_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
        data = response.json()
        return {"what": data}

@app.get("/new-token")
async def new_token():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open('.token.json', 'w') as token:
        token.write(creds.to_json())
    return {"token": creds.token}

@app.get("/tube-stats")
async def get_tube_stats():
    creds = Credentials.from_authorized_user_file('.token.json')
    access_token = creds.token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "filters": f"video=={VIDEO}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(VIEWS, headers=headers)
        return response.json()