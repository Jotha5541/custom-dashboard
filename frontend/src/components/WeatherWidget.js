import React, { useState, useEffect } from 'react';
import axios from 'axios'; 

function WeatherWidget() {
    const [weatherData, setWeatherData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchWeather = async () => {
            try {
                const apiUrl = `${process.env.REACT_APP_API_BASE_URL}/weather`;
                const response = await axios.get(apiUrl);
                setWeatherData(response.data);
            }
            catch (error) {
                console.error("Error while fetching weather data:", error);
            }
            finally {
                setLoading(false);
            }
        };

        fetchWeather();
    }, []);    // Empty array means this effect runs once

    if (loading) {
        return <div>Loading weather...</div>;
    }
    if (!weatherData) {
        return <div>No weather data available</div>;
    }

    return (
        <div className="weather-widget">
            <h2>Weather in {weatherData.name}</h2>
            <p>Temperature: {Math.round(weatherData.main.temp)}°F</p>
            <p>Condition: {weatherData.weather[0].description}</p>
        </div>
    );
}

export default WeatherWidget;