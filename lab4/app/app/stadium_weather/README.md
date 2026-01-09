1. Agent Name
Stadium Weather Expert

2. Agent Purpose
This agent is designed to act as a professional football match coordinator and weather analyst. It provides real-time meteorological conditions for major football stadiums by fetching live data directly from global weather APIs. It helps match officials and fans quickly determine if playing conditions are optimal (temperature, sky conditions) without manual searching.

3. Agent Tools
get_stadium_weather(stadium_city)
Description: A specialized meteorological tool that maps a city name to its primary world-class stadium's coordinates (e.g., London to Emirates Stadium).

Function: It uses the coordinates to query the Open-Meteo API and returns a formatted string containing the stadium name, current temperature in Celsius, and a weather condition status.

4. Example Interaction
User: "Check the weather for the game in Madrid tonight." Agent: (Decision: Triggers get_stadium_weather) Agent Output: "The current weather at Santiago Bernabéu (Madrid) is 18.5°C with clear skies. These are ideal conditions for a high-intensity football match!"
<img width="1572" height="608" alt="weatherChat" src="https://github.com/user-attachments/assets/0b8a2deb-ddf4-4a07-bdb8-32e607e93876" />
