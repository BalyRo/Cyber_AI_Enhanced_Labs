# 🏟️ stadium-weather-expert

## 1. Agent Name
`stadium-weather-expert`

## 2. Agent Purpose
The purpose of this agent is to demonstrate **basic agent development with tool usage** and to illustrate how responsibility is split between tools and the agent itself. 

This agent is designed to:
* **Interact with the user** about football match conditions in specific stadiums.
* **Retrieve structured information** via external weather APIs.
* **Reason about and explain** weather suitability for professional matches in natural language.

**Educational focus:**
* This agent operates on live, real-time meteorological data.
* It illustrates how an LLM can transform raw numerical data (temperature, codes) into actionable human advice.

## 3. Agent Tools
This agent uses a specialized tool to demonstrate efficient data retrieval and preparation.

### 3.1 get_stadium_weather(stadium_city)
**Purpose:** Provides a detailed overview of current weather conditions for a primary football stadium in a selected city.

**Output includes:**
* **Stadium Name:** (e.g., Emirates Stadium, Santiago Bernabéu).
* **Current Temperature:** Celsius degrees.
* **Weather Status:** Meteorological condition code.
* **Timestamp:** Time of the data retrieval.

**Design principle:** The tool returns **fully prepared metadata**, including the mapping of a city name to exact coordinates, allowing the agent to immediately reason about the playing conditions.

## 4. Tool–Agent Responsibility Split
This agent demonstrates the following fundamental rule of agentic design:
* **Tools** are responsible for data retrieval (API calls), geographic mapping, and structuring the raw meteorological response.
* **The Agent** is responsible for reasoning, explaining what the weather means for the players/fans, and interpretation.

**Examples:**
* **Tool:** Fetches the exact temperature and weather code from the API.
* **The Agent:** Explains if the temperature is ideal for a high-intensity match or
Example Interaction:
<img width="1572" height="608" alt="weatherChat" src="https://github.com/user-attachments/assets/0b8a2deb-ddf4-4a07-bdb8-32e607e93876" />
