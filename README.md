# Weather API

A Flask-based Weather API that fetches weather data from the Visual Crossing Weather API.

## Project URL

https://roadmap.sh/projects/weather-api-wrapper-service

## Features

* Third-party API integration
* Environment variables
* In-memory caching
* Rate limiting
* Error handling

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## Endpoint

GET /weather/<city>

Example:

GET /weather/Delhi

Example Response:

{
"city": "Delhi",
"conditions": "Partially cloudy",
"humidity": 52.6,
"temperature": 31.3
}

```
```
