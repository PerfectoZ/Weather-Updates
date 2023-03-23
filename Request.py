import http.client
import json

def Fetch():
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    payload = ''
    headers = {}
    locations = [
                    ["28.7932","77.0483"],
                    ["28.6189","77.2867"]
                ]
    responses = []
    for coord in locations :
        conn.request("GET", "/data/2.5/weather?lat="+coord[0]+"&lon="+coord[1]+"&appid=71b9f291c1f998aa5c3f962a5d0abfbd", payload, headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        json_data = json.loads(data)
        responses.append(json_data)
    return responses
