import requests

#retrieve the api key from a file 
apikey = open("path_to_apikey.txt").read()

#city location 
q = str(input("enter your city to view the weather:"))
city_name = q
#base url of the city location api " api key + q "
location_api = "http://dataservice.accuweather.com/locations/v1/cities/search?"
city_url = location_api + f"apikey={apikey}" +f"&q={q}"
city_response = requests.get(city_url)

#prints the city code that may be used for additional operations
if city_response.status_code == 200: 
    city_key = city_response.json()[0]["Key"]
    print(f"the city key is: " + city_key)
else: 
    print("Error", city_response.status_code)

#base url of the weather api 
weather_api = f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{city_key}?"

weather_url = weather_api + f"apikey={apikey}"
weather_response = requests.get(weather_url)

#print your response, you can specify what you want from the output json file : weather
if weather_response.status_code == 200: 
    weather = weather_response.json()
    date = weather[0]['DateTime'][0:10:]
    temperature = weather[0]["Temperature"]["Value"]
    #convert temp from f to C
    temperature = (temperature-32) * (5/9)
    print(f"the temperature in {city_name} for the next hour will be {round(temperature,1)}C, for today the {date} ")
else: 
    print("Error", city_response.status_code)

