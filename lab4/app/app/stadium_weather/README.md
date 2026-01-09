stadium-weather-expert
1. Agent Name
stadium-weather-expert

2. Agent Purpose
The purpose of this agent is to demonstrate real-time tool usage with external API integration and to illustrate the separation of concerns between data fetching (tools) and conversational reasoning (agent).

This agent is designed to:

Interact with users regarding football match conditions in specific global stadiums.

Retrieve live meteorological data via external tools.

Reason about weather suitability for professional football matches and explain it in natural language.

Educational focus:

This agent demonstrates how an LLM can use precise geographic coordinates to fetch non-static data.

It illustrates the transformation of raw API JSON responses into meaningful human advice.

3. Agent Tools
This agent uses a specialized tool that illustrates structured data retrieval from an external source.

3.1 get_stadium_weather(stadium_city)
Purpose: Provides live weather conditions for a primary football stadium in a given city.

Input:

stadium_city – The name of the city (e.g., "London", "Madrid", "Barcelona").

Output includes:

Stadium Name: The specific venue mapped to the city.

Temperature: Current temperature in Celsius.

Weather Code: Meteorological status code from the API.

Timestamp: The time of the observation.

Design principle: The tool is responsible for Coordinate Mapping (translating a city name to exact Latitude/Longitude) and API Communication, allowing the agent to focus on interpreting the results.

4. Tool–Agent Responsibility Split
This agent follows the fundamental rule of modern agentic workflows:

Tools are responsible for data retrieval (API calls), coordinate mapping, and error handling for external services.

The Agent is responsible for reasoning (deciding if 8°C is "too cold" for a game), explanation, and maintaining the persona of a football match coordinator.

Example:

Tool: Fetches raw numbers like temperature: 12.5.

Agent: Explains that "12.5°C is slightly brisk but excellent for high-intensity play; players should warm up thoroughly".
Example Interaction:
<img width="1572" height="608" alt="weatherChat" src="https://github.com/user-attachments/assets/0b8a2deb-ddf4-4a07-bdb8-32e607e93876" />
