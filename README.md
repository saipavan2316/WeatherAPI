# Weather API

A Flask Weather API using Visual Crossing Weather API.

## Project URL

https://roadmap.sh/projects/weather-api-wrapper-service
## Features

* Fetch weather data by city
* Visual Crossing API integration
* Environment variables
* In-memory caching
* Rate limiting
* Error handling

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Endpoint

```text
GET /weather/<city>
```

Example:

```text
/weather/Delhi
```

Example Response:

```json
{
  "city": "Delhi",
  "conditions": "Partially cloudy",
  "humidity": 52.6,
  "temperature": 31.3
}
```
