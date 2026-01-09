\# 1. Agent Name

Stadium Weather Expert Agent



\# 2. Agent Purpose

The Stadium Weather Expert is a specialized assistant for football match coordinators and fans. 

It helps determine real-time playing conditions in world-class stadiums (like Emirates, Bernabéu, and Camp Nou).

By using live weather data from an external API, the agent provides factual temperature and weather status instead of generating estimates.



\# 3. Agent Tools

\* \*\*get\_stadium\_weather(stadium\_city)\*\*:

&nbsp;   - \*\*What the tool does\*\*: Maps a city name to its specific stadium coordinates and fetches live meteorological data using the Open-Meteo API.

&nbsp;   - \*\*Input\*\*: The name of the city (string) - currently supports "London", "Madrid", or "Barcelona".

&nbsp;   - \*\*Output\*\*: A detailed string containing the stadium name, current temperature in Celsius, and a weather condition code.



\# 4. Example Interaction

\*\*User\*\*: "Is it too cold to play in London today?"

\*\*Agent\*\*: \[Action: Invokes get\_stadium\_weather(stadium\_city="London")]

\*\*Agent\*\*: "The current weather at Emirates Stadium (London) is 8°C. While it's a bit chilly, it's still suitable for a professional match. Don't forget to advise players to stay warm!"



\*\*User\*\*: "Check Madrid for me."

\*\*Agent\*\*: \[Action: Invokes get\_stadium\_weather(stadium\_city="Madrid")]

\*\*Agent\*\*: "Weather at Santiago Bernabéu (Madrid): 18°C. Status code: 0. These are perfect conditions for a high-intensity football match."

<img width="1572" height="608" alt="weatherChat" src="https://github.com/user-attachments/assets/0b8a2deb-ddf4-4a07-bdb8-32e607e93876" />
