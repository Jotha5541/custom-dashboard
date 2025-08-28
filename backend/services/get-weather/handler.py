import json
import os
import requests

def get_weather(event, context):
    
    # Get API Key from environment variable
    api_key = os.environ.get('WEATHER_API_KEY')
    if not api_key:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'API key not configured'})
        }
    
    city = "Corona, CA" # Hardcoded city for now
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    
    print(f"Constructed URL: {url}")
    try:
        response = requests.get(url)    # GET request
        response.raise_for_status()     # Raise error and triggers exception
        weather_data = response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error calling Weather API: {e}")
        return {
            'statusCode': 502,
            'body': json.dumps({'error': f"Error fetching weather data."})
        }
    
    return {
        'statusCode': 200,  # Successful request
        "headers": {
            "Access-Control-Allow-Origin": "*",     # Indicate safe for frontend to access API
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(weather_data)
    }