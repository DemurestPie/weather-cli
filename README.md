# Python Weather CLI Program

This is a simple command-line application that retrieves weather information using the OpenWeatherMap API. The program allows users to get weather details by providing a ZIP code, city and state, or geographic coordinates (latitude and longitude). The results include temperature, humidity, weather description, and more.

## Features

- Get current weather by ZIP code
- Get current weather by geographic coordinates (latitude and longitude)
- Get current weather by city and state
- Clear console between actions for better readability
- Simple text-based menu for easy navigation

## Requirements

- Python 3.x
- `requests` library (You can install it via `pip install requests`)

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/demurestpie/weather-cli.git
   cd weather-cli
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

3. Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

4. Replace the `API_KEY` in the script with your OpenWeatherMap API key.

   ```python
   API_KEY = "your_openweathermap_api_key"
   ```

5. Run the program:

   ```bash
   python weather.py
   ```

## Program Settings

- **Units for Temperature:** The temperature is displayed in Fahrenheit (`imperial` units). You can modify the `units` variable in the code to `metric` (Celsius) or `standard` (Kelvin) if needed.
- **Country Code:** The default country code is set to `"US"`. You can change this if you need weather for cities in other countries.

## How It Works

### 1. Get Weather by ZIP Code

- Select the option `1` from the menu.
- Enter a valid ZIP code (e.g., `37601`).
- The program will display the weather details for the location associated with that ZIP code.

### 2. Get Weather by Coordinates

- Select the option `2` from the menu.
- Enter the latitude and longitude values for the location (e.g., `36.3134`, `-82.3535`).
- The program will retrieve and display the weather for those geographic coordinates.

### 3. Get Weather by City and State

- Select the option `3` from the menu.
- Enter the city name and state abbreviation (e.g., `Johnson City`, `TN`).
- The program will fetch the weather details for that city.

### 4. Exit

- Choose option `4` to exit the program.

## Error Handling

- The program handles invalid inputs (e.g., non-numeric ZIP codes or coordinates).
- If the weather data cannot be retrieved due to a network error or invalid API key, the program will display the relevant HTTP status code and error message.
