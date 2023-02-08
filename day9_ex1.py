travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_dict = {
        "country" : country,
        "visits" : visits,
        "cities" : cities
    }
    travel_log.append(new_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Italia", 2, ["Milan", "Roma", "Venezia"])
print(travel_log)
