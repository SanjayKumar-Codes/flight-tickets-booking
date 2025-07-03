import sys
import os
from .processor import process_flight_data
from .scraper import fetch_flight_data 
from fastapi.staticfiles import StaticFiles
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import Form

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)



app.mount("/static", StaticFiles(directory="app/static"), name="static")



@app.api_route("/", methods=["GET", "POST"], response_class=HTMLResponse)
async def home(request: Request, origin_country: str = Form(None)):
    df = fetch_flight_data()
    insights = process_flight_data(df)

    flights = []
    selected_country = None

    if request.method == "POST" and origin_country:
        filtered_flights = df[df["origin_country"] == origin_country][["callsign", "origin_country", "longitude", "latitude"]]
        flights = filtered_flights.to_dict(orient="records")
        selected_country = origin_country

    return templates.TemplateResponse("index.html", {
        "request": request,
        "insights": insights,
        "flights": flights,
        "selected_country": selected_country
    })



