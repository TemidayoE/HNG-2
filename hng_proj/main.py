from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI()

GEOLOCATION_API_URL =  "https://ipinfo.io/json"

WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "7055a238f3b6dea93e3d5099b152d7d4"

@app.get("/api/home")
async def home(request: Request, visitor_name: str):
    
    client_ip = request.client.host  
  
    async with httpx.AsyncClient() as client:
        geo_response = await client.get(GEOLOCATION_API_URL.format(ip=client_ip))
        geo_data = geo_response.json()

    city = geo_data.get("city", "Unknown Location")

   
    lat, lon = geo_data.get("loc", "0,0").split(',')
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": WEATHER_API_KEY,
        "units": "metric"  
    }

    async with httpx.AsyncClient() as client:
        weather_response = await client.get(WEATHER_API_URL, params=weather_params)
        weather_data = weather_response.json()

   
    temperature = weather_data.get("main", {}).get("temp", 0)

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"

    return {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }
