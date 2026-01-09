import os
import json
import urllib.request
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

def get_stadium_weather(stadium_city: str) -> str:
    """Retrieves real-time weather for football stadiums in specific cities."""
  
    stadiums = {
        "London": {"lat": 51.55, "lon": -0.10, "name": "Emirates Stadium"},
        "Madrid": {"lat": 40.45, "lon": -3.68, "name": "Santiago Bernabéu"},
        "Barcelona": {"lat": 41.38, "lon": 2.12, "name": "Camp Nou"}
    }
    
    city_data = stadiums.get(stadium_city)
    if not city_data:
        return f"No stadium data found for {stadium_city}. Try London, Madrid or Barcelona."

    url = f"https://api.open-meteo.com/v1/forecast?latitude={city_data['lat']}&longitude={city_data['lon']}&current_weather=true"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            temp = data["current_weather"]["temperature"]
            condition_code = data["current_weather"]["weathercode"]
            return f"Weather at {city_data['name']} ({stadium_city}): {temp}°C. Status code: {condition_code}."
    except Exception as e:
        return f"Weather API Error: {str(e)}"

# המוח: חיבור ל-Groq/OpenAI 
client = OpenAIChatClient(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY"),
    model_id=os.getenv("MODEL")
)


football_weather_bot = ChatAgent(
    chat_client = client,
    name="Stadium Weather Expert",
    instructions="""
        You are a football match coordinator. 
        Your job is to check the weather conditions for matches in major stadiums.
        When asked about the weather in London, Madrid or Barcelona, you MUST use the 
        'get_stadium_weather' tool.
    """,
    tools=[get_stadium_weather],
    additional_chat_options={
            "timeout": 60.0
    }
)


agent = football_weather_bot