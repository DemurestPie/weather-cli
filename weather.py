import requests
from dotenv import load_dotenv
import os
import datetime

# Load environment variables
load_dotenv()

## PROGRAM SETTINGS
# Units for temperature (standard for kevin, imperial for fahrenheit, metric for celsius)
units = "imperial"
# Country code
country = "US"
# API key
API_KEY = os.getenv("API_KEY")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get weather by zipcode
def get_weather_by_zipcode(zipcode):

    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country}&units={units}&appid={API_KEY}"

    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print_weather(response.json())
    else:
        print(f"Failed to retrieve details. HTTP Status code: {response.status_code}")

# Function to get weather by coordinates
def get_weather_by_coordinates(lat, lon):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={API_KEY}"

    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print_weather(response.json())
    else:
        print(f"Failed to retrieve details. HTTP Status code: {response.status_code}")


# Function to get weather by city and state
def get_weather_by_city(city, state):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&units={units}&appid={API_KEY}"

    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print_weather(response.json())
    else:
        print(f"Failed to retrieve details. HTTP Status code: {response.status_code}")

# Function to print weather details
def print_weather(response):
    print(f"Weather for {response['name']}:")
    print(f"{'-' * 20}")
    print(f"Temperature: {round(response['main']['temp'])}°F")
    print(f"Feels like: {round(response['main']['feels_like'])}°F")
    print(f"Description: {response['weather'][0]['description'].capitalize()}")
    print(f"High: {round(response['main']['temp_max'])}°F")
    print(f"Low: {round(response['main']['temp_min'])}°F")
    print(f"Humidity: {response['main']['humidity']}%")
    print(f"Pressure: {response['main']['pressure']} hPa")
    print(f"Visibility: {response['visibility']} meters")
    print(f"Wind Speed: {response['wind']['speed']} m/s")
    
    # Convert sunrise and sunset times from Unix to readable format
    sunrise = datetime.datetime.fromtimestamp(response['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(response['sys']['sunset']).strftime('%H:%M:%S')
    
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")


def main():

    def get_int_input(prompt):
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_int_input(prompt)
        
    def get_float_input(prompt):
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_float_input(prompt)


    while True:
        print("Weather API")
        print("1. Get weather by zipcode")
        print("2. Get weather by coordinates")
        print("3. Get weather by city")
        print("4. Exit")
        choice = get_int_input("Enter choice: ")
        clear_console()

        if choice == 1:
            zipcode = get_int_input("Enter zipcode: ")
            get_weather_by_zipcode(zipcode)
            input("Press enter to continue...")
            clear_console()
        elif choice == 2:
            lat = get_float_input("Enter latitude: ")
            lon = get_float_input("Enter longitude: ")
            get_weather_by_coordinates(lat, lon)
            input("Press enter to continue...")
            clear_console()
        elif choice == 3:
            city = input("Enter city: ")
            state = input("Enter state code (ex: TN, NC): ")
            get_weather_by_city(city, state)
            input("Press enter to continue...")
            clear_console()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press enter to continue...")
            clear_console()
    

if __name__ == "__main__":
    main()
