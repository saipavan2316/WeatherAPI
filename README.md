# Weather API

A Flask-based Weather API that fetches weather data from the Visual Crossing Weather API.

## Project URL

http://127.0.0.1:5000/weather/Delhi

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
