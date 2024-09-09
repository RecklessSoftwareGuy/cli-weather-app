import requests, json, sys

config = json.load(open('assets/config.json'))
key=config['api-key']
output = ''
weather_info = []
location= "New Delhi"

weather = requests.get(url=f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&days=1")
forecast = requests.get(url=f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days=1&aqi=yes&alerts=no")

if weather.status_code == 200:
    response1= weather.text
    res1 = json.loads(response1)
    response2= forecast.text
    res2= json.loads(response2)

    print("Location: "+res1['location']['name'])
    print("Time: " + res1['location']['localtime'])
    print(f"Temperature: {res1['current']['temp_c']}")
    print(f"Feels like: {res1['current']['feelslike_c']}")
    print(f"Condition: {res1['current']['condition']['text']}")
    print(f"Rainfall : {res1['current']['precip_mm']}")
    # print(f"Forecast : {res2['forecast']['forecastday']['day']['condition']['text']}")
    # print(f"Air-Quality-Index (Insternational Standard): {res['current']['air_quality']['gb-defra-index']}")


else:
    print("Invalid API key")