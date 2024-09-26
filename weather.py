import requests
import os

## PROGRAM SETTINGS
# Units for temperature (standard for kevin, imperial for fahrenheit, metric for celsius)
units = "imperial"
# Country code
country = "US"
# API key
API_KEY = "your_openweathermap_api_key"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get weather by zipcode
def get_weather_by_zipcode(zipcode):

    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country}&units=imperial&appid={API_KEY}"

    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML response and display the result
        print(f"Weather for {response.json()['name']}:")
        print(f"{"-" * 20}")
        print(f"Temperature: {round(response.json()['main']['temp'])}°F")
        print(f"Feels like: {round(response.json()['main']['feels_like'])}°F")
        print(f"Description: {response.json()['weather'][0]['description']}")
        print(f"High: {round(response.json()['main']['temp_max'])}°F")
        print(f"Low: {round(response.json()['main']['temp_min'])}°F")
        print(f"Humidity: {response.json()['main']['humidity']}%")
    else:
        print(f"Failed to retrieve details. HTTP Status code: {response.status_code}")

# Function to get weather by coordinates
def get_weather_by_coordinates(lat, lon):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={API_KEY}"

    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML response and display the result
        print(f"Weather for {response.json()['name']}:")
        print(f"{"-" * 20}")
        print(f"Temperature: {round(response.json()['main']['temp'])}°F")
        print(f"Feels like: {round(response.json()['main']['feels_like'])}°F")
        print(f"Description: {response.json()['weather'][0]['description']}")
        print(f"High: {round(response.json()['main']['temp_max'])}°F")
        print(f"Low: {round(response.json()['main']['temp_min'])}°F")
        print(f"Humidity: {response.json()['main']['humidity']}%")
    else:
        print(f"Failed to retrieve details. HTTP Status code: {response.status_code}")


# Function to get weather by city and state
def get_weather_by_city(city, state):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&units=imperial&appid={API_KEY}"

    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML response and display the result
        print(f"Weather for {response.json()['name']}:")
        print(f"{"-" * 20}")
        print(f"Temperature: {round(response.json()['main']['temp'])}°F")
        print(f"Feels like: {round(response.json()['main']['feels_like'])}°F")
        print(f"Description: {response.json()['weather'][0]['description']}")
        print(f"High: {round(response.json()['main']['temp_max'])}°F")
        print(f"Low: {round(response.json()['main']['temp_min'])}°F")
        print(f"Humidity: {response.json()['main']['humidity']}%")
    else:
        print(f"Failed to retrieve details. HTTP Status code: {response.status_code}")


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
