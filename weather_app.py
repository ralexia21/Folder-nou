import requests

def get_weather(city):
    url= f"https://wttr.in/{city}?format=j1"
    response= requests.get(url)
    data= response.json()
    temp= data["current_condition"][0]["temp_C"]
    description= data["current_condition"][0]["weatherDesc"][0]["value"]
    print(f"\nWeather in {city}: ")
    print(f"Temperature: {temp}C")
    print(f"Condition: {description}")

city= input("city: ")
get_weather(city)