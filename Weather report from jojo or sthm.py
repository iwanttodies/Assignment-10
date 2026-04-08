import requests 

def weather(city,code):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={code}"
    try:
        respond=requests.get(url)
        data=respond.json()

        cityname=data['name']
        description = data["weather"][0]["description"]
        kelvin = data["main"]["temp"]

        Celsius=kelvin-273

        print(f"City:        {cityname}")
        print(f"Condition:   {description}")
        print(f"Temperature: {Celsius:.1f}°C")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong brotato: {e}")
    except KeyError:
        print("Make sure use the right spelling for the city name or it won't return anything lmao")

api_key="9a99a7b6aba4ee8ce9e2ca77660dff2d"

res_city=input("Enter your city: ")

weather(res_city,api_key)


