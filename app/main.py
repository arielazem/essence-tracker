from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

GIST_URL = "https://gist.githubusercontent.com/arielazem/1b60ce27fe3da96153d8acdfbbdcfc9f/raw/77c692dbf5c0ecf732f275043bba996bafbbe62b/habits.json"

async def load_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(GIST_URL)
        response.raise_for_status()
        return response.json()["identities"]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    identities = await load_data()
    return templates.TemplateResponse("index.html", {"request": request, "identities": identities})

@app.get("/identity/{identity_id}", response_class=HTMLResponse)
async def identity_detail(identity_id: str, request: Request):
    identities = await load_data()
    identity = next((i for i in identities if i["id"] == identity_id), None)
    if not identity:
        raise HTTPException(status_code=404, detail="Identity not found")
    return templates.TemplateResponse("identity_detail.html", {"request": request, "identity": identity})