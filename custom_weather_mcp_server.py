import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP


# ============================================================
# Configuration
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

# Load .env from the same directory as this file
load_dotenv(BASE_DIR / ".env")

mcp = FastMCP("Weather MCP Server")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
REQUEST_TIMEOUT_SECONDS = 20

CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


# ============================================================
# Helper Functions
# ============================================================

def _get_api_key() -> str:
    """Return the OpenWeather API key or raise a clear error."""
    if not OPENWEATHER_API_KEY:
        raise RuntimeError(
            "OPENWEATHER_API_KEY is missing from the project .env file."
        )

    return OPENWEATHER_API_KEY


def _request_json(
    url: str,
    params: dict[str, Any],
) -> dict[str, Any]:
    """Make an HTTP GET request and return the JSON response."""
    try:
        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as exc:
        details = ""

        failed_response = getattr(exc, "response", None)

        if failed_response is not None:
            details = (
                f" Response: {failed_response.text[:500]}"
            )

        raise RuntimeError(
            f"OpenWeather request failed: {exc}.{details}"
        ) from exc


# ============================================================
# MCP Tools
# ============================================================

@mcp.tool()
def get_current_weather(city: str) -> dict[str, Any]:
    """
    Return the current weather for a city.

    Args:
        city: City name, for example "Delhi" or "London".
    """
    city = city.strip()

    if not city:
        raise ValueError("city cannot be empty")

    data = _request_json(
        CURRENT_WEATHER_URL,
        {
            "q": city,
            "appid": _get_api_key(),
            "units": "metric",
        },
    )

    return {
        "city": data["name"],
        "country": data.get("sys", {}).get("country"),
        "temperature_c": data["main"]["temp"],
        "feels_like_c": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "wind_speed_mps": data["wind"]["speed"],
    }


@mcp.tool()
def get_forecast(city: str) -> dict[str, Any]:
    """
    Return the first five three-hour forecast entries for a city.

    Args:
        city: City name, for example "Delhi" or "London".
    """
    city = city.strip()

    if not city:
        raise ValueError("city cannot be empty")

    data = _request_json(
        FORECAST_URL,
        {
            "q": city,
            "appid": _get_api_key(),
            "units": "metric",
        },
    )

    forecast = [
        {
            "datetime": item["dt_txt"],
            "temperature_c": item["main"]["temp"],
            "feels_like_c": item["main"]["feels_like"],
            "humidity": item["main"]["humidity"],
            "condition": item["weather"][0]["description"],
            "wind_speed_mps": item["wind"]["speed"],
        }
        for item in data.get("list", [])[:5]
    ]

    return {
        "city": data.get("city", {}).get("name", city),
        "country": data.get("city", {}).get("country"),
        "forecast": forecast,
    }


# ============================================================
# MCP Server Entry Point
# ============================================================

if __name__ == "__main__":
    # STDIO is intended for an MCP client that starts this
    # server as a subprocess.
    #
    # Example:
    # TripMate MCP Client
    #       |
    #       | STDIO
    #       v
    # Weather MCP Server
    #
    # Explicitly specifying stdio is supported by FastMCP.
    mcp.run(transport="stdio")
