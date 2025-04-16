# write a small and simple program using the requests library to call the API,
#  parse the JSON and display that JSON in a meaningful way. 
# You can make this as simple or complex as you have time for.
import json
data = {
    "weather":"https://api.open-meteo.com/v1/forecast?"
}

print(f'weather{data}:[weather]')
